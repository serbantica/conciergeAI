# services/knowledge_service.py
from transformers import pipeline
import requests

# LLM-based Inference Function
class KnowledgeInference:
    def __init__(self, model_name="deepset/roberta-base-squad2"):
        self.qa_pipeline = pipeline("question-answering", model=model_name)

    def get_answer(self, question: str, context: str):
        """
        This function queries the LLM model to get answers to questions
        based on a given context (e.g., a document, knowledge base, etc.)
        """
        result = self.qa_pipeline({
            'question': question,
            'context': context
        })
        return result['answer']


# External Knowledge Service Function
class KnowledgeService:
    def __init__(self, api_url="https://example.com/api"):
        self.api_url = api_url

    def fetch_data(self):
        """
        This function fetches data from an external service (API).
        The returned data could be related to the knowledge the agent needs
        to process requests.
        """
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data"}

    def process_external_data(self, data):
        """
        This function processes data received from an external source,
        performing necessary transformations or filtering before it's used.
        """
        # Perform any transformations, e.g., filter out unwanted information
        processed_data = {key: value for key, value in data.items() if key != "unwanted_key"}
        return processed_data


# Main Knowledge Agent Service (combining LLM and external data services)
class KnowledgeAgentService:
    def __init__(self):
        self.inference = KnowledgeInference()  # LLM-based inference
        self.service = KnowledgeService()  # External data services

    def process_request(self, query, context=None):
        """
        This function processes the request for the Knowledge Agent.
        It either uses LLM inference (if a query and context are provided)
        or fetches external data from a service if no context is available.
        """
        if query and context:
            # Use LLM-based inference for answering questions
            return self.inference.get_answer(query, context)
        else:
            # Fetch data from an external service when no context is provided
            data = self.service.fetch_data()
            return data


# Example usage:
if __name__ == "__main__":
    knowledge_agent = KnowledgeAgentService()

    # Example 1: Using LLM-based inference
    context = "The Eiffel Tower is located in Paris and is 330 meters tall."
    question = "Where is the Eiffel Tower located?"
    print(knowledge_agent.process_request(question, context))

    # Example 2: Fetching data from an external service
    print(knowledge_agent.process_request(query=None))

# knowledge_agent.py
from services.knowledge_service import KnowledgeAgentService

class KnowledgeAgent:
    def __init__(self):
        self.agent_service = KnowledgeAgentService()  # Initialize the KnowledgeAgentService

    def answer_question(self, question, context=None):
        """
        Main function to process a query. This will interact with the
        KnowledgeAgentService to get answers from either LLM inference or external data.
        """
        response = self.agent_service.process_request(question, context)
        return response


# Example usage:
if __name__ == "__main__":
    knowledge_agent = KnowledgeAgent()

    # Example 1: Asking a question with a context (LLM-based)
    context = "The Eiffel Tower is located in Paris and is 330 meters tall."
    question = "Where is the Eiffel Tower located?"
    print(f"Answer: {knowledge_agent.answer_question(question, context)}")

    # Example 2: Fetching data from external service (no context, just data)
    print(f"External Data: {knowledge_agent.answer_question(None)}")

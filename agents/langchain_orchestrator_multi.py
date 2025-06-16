# orchestrator_agent.py
from langchain.agents import AgentExecutor
from services.knowledge_service import KnowledgeAgent
from services.planning_service import PlanningAgent
from services.wellbeing_service import WellbeingAgent
from langchain.llms import OpenAI

class OrchestratorAgent:
    def __init__(self):
        # Initialize LangChain LLM
        self.llm = OpenAI(temperature=0)
        
        # Initialize Agents
        self.knowledge_agent = KnowledgeAgent(self.llm)
        self.planning_agent = PlanningAgent(self.llm)
        self.wellbeing_agent = WellbeingAgent(self.llm)

        # Define tools for each agent
        self.tools = [
            self.knowledge_agent.tools[0],
            self.planning_agent.tools[0],
            self.wellbeing_agent.tools[0]
        ]
        
        # Initialize AgentExecutor for multi-agent orchestration
        self.executor = AgentExecutor(
            tools=self.tools,
            llm=self.llm,
            agent_type="zero-shot-react-description",
            verbose=True
        )

    def execute(self, user_input: str):
        # Execute the agent executor based on user input
        return self.executor.run(user_input)

# Example usage:
if __name__ == "__main__":
    orchestrator = OrchestratorAgent()
    
    # Example: Multi-agent workflow execution
    print(orchestrator.execute("Tell me how to stay healthy and plan my day"))

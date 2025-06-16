# services/planning_service.py
from langchain.agents import Tool
from langchain.llms import OpenAI
from langchain.agents import initialize_agent

class PlanningAgent:
    def __init__(self, llm: OpenAI):
        self.llm = llm
        self.tools = [
            Tool(
                name="planning_tool",
                func=self.plan_task,
                description="Tool to manage and plan tasks."
            ),
        ]
    
    def plan_task(self, task_description: str):
        # Custom function to plan tasks
        return f"Plan for: {task_description}"

    def process_request(self, user_input: str):
        # Integrate with LangChain’s agent system to handle requests
        agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent_type="zero-shot-react-description",
            verbose=True
        )
        return agent.run(user_input)

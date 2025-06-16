# orchestrator_agent.py
from services.knowledge_service import KnowledgeAgentService
from services.planning_service import PlanningAgentService
from services.wellbeing_service import WellbeingAgentService
from events import Event, EventHandler

class OrchestratorAgent:
    def __init__(self):
        # Initialize all agents involved in the system
        self.knowledge_agent = KnowledgeAgentService()  # Knowledge-based agent
        self.planning_agent = PlanningAgentService()  # Planning agent for task management
        self.wellbeing_agent = WellbeingAgentService()  # Wellbeing agent for health & fitness
        
        # Register event handlers
        self.event_handler = EventHandler()
        self.event_handler.register('knowledge_event', self.knowledge_agent.process_request)
        self.event_handler.register('planning_event', self.planning_agent.process_request)
        self.event_handler.register('wellbeing_event', self.wellbeing_agent.process_request)

    def route_event(self, event_name, *args, **kwargs):
        """
        Routes the event to the appropriate agent based on the event name.
        """
        return self.event_handler.handle(event_name, *args, **kwargs)


# events.py (Event and EventHandler for modular event-driven handling)
class Event:
    def __init__(self, name):
        self.name = name


class EventHandler:
    def __init__(self):
        self._handlers = {}

    def register(self, event_name, handler):
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)

    def handle(self, event_name, *args, **kwargs):
        handlers = self._handlers.get(event_name, [])
        results = []
        for handler in handlers:
            results.append(handler(*args, **kwargs))
        return results


# Example usage:
if __name__ == "__main__":
    orchestrator = OrchestratorAgent()

    # Example: Handling a knowledge event
    knowledge_event = Event('knowledge_event')
    context = "The Eiffel Tower is located in Paris and is 330 meters tall."
    print(f"Response: {orchestrator.route_event('knowledge_event', 'Where is the Eiffel Tower?', context)}")

    # Example: Handling a planning event
    planning_event = Event('planning_event')
    print(f"Response: {orchestrator.route_event('planning_event', 'Can you schedule my workout for tomorrow?')}")
    
    # Example: Handling a wellbeing event
    wellbeing_event = Event('wellbeing_event')
    print(f"Response: {orchestrator.route_event('wellbeing_event', 'What should I eat for a healthy diet?')}")

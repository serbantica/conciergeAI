import openai
from transformers import pipeline

class LLMManager:
    def __init__(self, config):
        self.config = config
        self.models = self.load_models()

    def load_models(self):
        models = {}
        for model_name, details in self.config.items():
            if details['type'] == 'openai':
                models[model_name] = lambda prompt: openai.Completion.create(
                    engine=details['engine'], prompt=prompt
                )
            elif details['type'] == 'transformers':
                models[model_name] = pipeline(details['task'], model=details['model_name'])
        return models

    def invoke_model(self, model_name, input_data):
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not configured.")
        return self.models[model_name](input_data)

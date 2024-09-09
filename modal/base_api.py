import google.generativeai as genai
class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def initialise_model(self, model_name="gemini-1.5-pro"):
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(model_name)
        return model
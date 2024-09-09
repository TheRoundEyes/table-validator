from modal.base_api import GeminiAPI


class Chat(GeminiAPI):
    def __init__(self, api_key):
        super().__init__(api_key)

    def chat_with_model(self,query,model):
        response = model.generate_content(query)
        return response
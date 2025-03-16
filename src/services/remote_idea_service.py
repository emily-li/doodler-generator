from .abstract_idea_service import AbstractIdeaService
from models.api import RemoteIdeaRequest
import os
from dotenv import load_dotenv
import requests


class RemoteIdeaService(AbstractIdeaService):

    def generate(self, request: RemoteIdeaRequest) -> str:
        load_dotenv()

        payload = {
            "model": request.model_name,
            "messages": self.get_chat_template(),
            "repetition_penalty": request.repetition_penalty,
            "temperature": request.temperature,
            "top_p": request.top_p,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('API_KEY')}",
        }

        response = requests.request(
            "POST",
            "https://api.arliai.com/v1/chat/completions",
            headers=headers,
            json=payload,
        )

        print(response)

        return response.json()["choices"][0]["message"]["content"]

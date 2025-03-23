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

        try:
            response = requests.request(
                "POST",
                f"https://api.{os.getenv('API')}.com/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=5,
            )
            print(response)
            response.raise_for_status()

        except requests.Timeout as e:
            print(f"Request timed out: {str(e)}")
            return ""
        except requests.HTTPError as e:
            print(f"HTTP error occurred: {str(e)}")
            return ""

        return response.json()["choices"][0]["message"]["content"]

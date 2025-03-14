from .abstract_idea_service import AbstractIdeaService
from models.api import RemoteIdeaRequest
import os
from openai import OpenAI
from dotenv import load_dotenv


class RemoteIdeaService(AbstractIdeaService):

    def generate(self, request: RemoteIdeaRequest) -> str:
        load_dotenv()

        client = OpenAI(
            base_url="https://api.aimlapi.com/v1",
            api_key=os.getenv("API_KEY"),
        )

        response = client.chat.completions.create(
            model=request.model_name,
            messages=self.get_chat_template(),
        )

        return response.choices[0].message.content

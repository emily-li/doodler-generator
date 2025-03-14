from abc import ABC, abstractmethod
from models.api import RemoteIdeaRequest


class AbstractIdeaService(ABC):
    """
    Generates a creative doodle idea text.

    Returns:
        str: A generated doodle idea text
    """

    @abstractmethod
    def generate(self, request: RemoteIdeaRequest) -> str:
        pass

    @staticmethod
    def get_chat_template() -> str:
        # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
        return [
            {
                "role": "system",
                "content": (
                    "You are a creative art teacher. Respond with a single concise and fun doodle idea. Your response should be less than 10 words and end with a period."
                ),
            },
            {"role": "user", "content": "Give me a doodle idea."},
            {"role": "assistant", "content": "A sleepy cat in a cardboard box."},
            {"role": "user", "content": "Another doodle idea please."},
            {
                "role": "assistant",
                "content": "A whale swimming with a small child holding its hand.",
            },
            {"role": "user", "content": "One more doodle idea."},
        ]

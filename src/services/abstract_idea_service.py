from abc import ABC, abstractmethod
from models.api import IdeaRequest


class AbstractIdeaService(ABC):
    """
    Generates a creative doodle idea text.

    Returns:
        str: A generated doodle idea text
    """

    @abstractmethod
    def generate(self, request: IdeaRequest) -> str:
        pass

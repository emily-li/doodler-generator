from dataclasses import dataclass
from abc import ABC


@dataclass
class AbstractIdeaRequest(ABC):
    model_name: str
    temperature: float
    top_p: float
    repetition_penalty: float


@dataclass
class LocalIdeaRequest(AbstractIdeaRequest):
    model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v0.6"
    temperature: float = 0.7
    top_p: float = 0.9
    repetition_penalty: float = 1.2


@dataclass
class RemoteIdeaRequest(AbstractIdeaRequest):
    model_name: str = "Mistral-Nemo-12B-Instruct-2407"
    temperature: float = 0.9
    top_p: float = 0.9
    repetition_penalty: float = 1.3


@dataclass
class IdeaResponse:
    idea: str

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class AbstractIdeaRequest(ABC):
    model_name: str


@dataclass
class LocalIdeaRequest(AbstractIdeaRequest):
    model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v0.6"
    max_new_tokens: int = 20
    do_sample: bool = True
    temperature: float = 0.7
    top_p: float = 0.9
    repetition_penalty: float = 1.2


@dataclass
class RemoteIdeaRequest(AbstractIdeaRequest):
    model_name: str = "gpt-4o"


@dataclass
class IdeaResponse:
    idea: str

from dataclasses import dataclass


@dataclass
class IdeaRequest:
    model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v0.6"
    max_new_tokens: int = 20
    do_sample: bool = True
    temperature: float = 0.7
    top_p: float = 0.9
    repetition_penalty: float = 1.2


@dataclass
class IdeaResponse:
    idea: str

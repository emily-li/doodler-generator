from .abstract_idea_service import AbstractIdeaService
from models.api import IdeaRequest
from transformers import pipeline
import torch
import re


class LocalIdeaService(AbstractIdeaService):

    def generate(self, request: IdeaRequest) -> str:
        # https://huggingface.co/docs/transformers/main_classes/pipelines
        generator = pipeline(
            "text-generation",
            model=request.model_name,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        messages = self._get_chat_template()
        prompt = generator.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        idea = generator(
            prompt,
            max_new_tokens=request.max_new_tokens,
            do_sample=request.do_sample,
            temperature=request.temperature,
            top_p=request.top_p,
            repetition_penalty=request.repetition_penalty,
            pad_token_id=generator.tokenizer.eos_token_id,
            eos_token_id=generator.tokenizer.eos_token_id,
            return_full_text=False,
        )[0]["generated_text"]
        return idea

    def _get_chat_template(self) -> str:
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

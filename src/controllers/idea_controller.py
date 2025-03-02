import torch
import re
from transformers import pipeline
from models.idea import Idea


class IdeaController:
    prompt: str
    generator: pipeline

    def __init__(self):
        # https://huggingface.co/docs/transformers/main_classes/pipelines
        self.generator = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v0.6",
            torch_dtype=torch.float16,
            device_map="auto",
        )

        # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
        messages = [
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
        self.prompt = self.generator.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )

    def get_idea(self) -> Idea:
        idea = self.generate_idea()
        return Idea(clean_idea(idea))

    # https://huggingface.co/docs/transformers/v4.49.0/main_classes/text_generation
    def generate_idea(self) -> str:
        return self.generator(
            self.prompt,
            max_new_tokens=20,
            do_sample=True, 
            top_p=0.9, 
            repetition_penalty=1.2,
            pad_token_id=self.generator.tokenizer.eos_token_id,
            eos_token_id=self.generator.tokenizer.eos_token_id,
            return_full_text=False,
        )[0]["generated_text"]

def clean_idea(idea: str) -> str:
    match = re.search(r"[.!?]", idea)
    if match:
        return idea[: match.start() + 1]
    else:
        return idea

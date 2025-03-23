from .abstract_idea_service import AbstractIdeaService
from models.api import LocalIdeaRequest


class LocalIdeaService(AbstractIdeaService):

    def generate(self, request: LocalIdeaRequest) -> str:
        from transformers import pipeline
        import torch

        # https://huggingface.co/docs/transformers/main_classes/pipelines
        generator = pipeline(
            "text-generation",
            model=request.model_name,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        messages = self.get_chat_template()
        prompt = generator.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        idea = generator(
            prompt,
            max_new_tokens=20,
            do_sample=True,
            temperature=request.temperature,
            top_p=request.top_p,
            repetition_penalty=request.repetition_penalty,
            pad_token_id=generator.tokenizer.eos_token_id,
            eos_token_id=generator.tokenizer.eos_token_id,
            return_full_text=False,
        )[0]["generated_text"]
        return idea

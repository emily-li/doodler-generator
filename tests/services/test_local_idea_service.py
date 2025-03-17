import pytest
from unittest.mock import Mock, patch
from src.services.local_idea_service import LocalIdeaService
from src.models.api import LocalIdeaRequest

expected_idea = "A happy cat playing with yarn."


@pytest.fixture
def mock_pipeline():
    with patch("src.services.local_idea_service.pipeline") as mock:
        mock_generator = Mock()
        mock_generator.return_value = [{"generated_text": expected_idea}]
        mock_generator.tokenizer.apply_chat_template.return_value = "mocked prompt"
        mock_generator.tokenizer.eos_token_id = 234
        mock.return_value = mock_generator
        yield mock


@pytest.fixture
def service():
    return LocalIdeaService()


def test_generate_returns_idea_with_defaults(mock_pipeline, service):
    request = LocalIdeaRequest()

    result = service.generate(request)

    assert result == expected_idea
    mock_pipeline.assert_called_once_with(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v0.6",
        torch_dtype=pytest.importorskip("torch").float16,
        device_map="auto",
    )
    mock_pipeline.return_value.assert_called_once_with(
        "mocked prompt",
        max_new_tokens=20,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        pad_token_id=234,
        eos_token_id=234,
        return_full_text=False,
    )
    _assert_chat_template(mock_pipeline)


def test_generate_returns_idea_with_request_params(mock_pipeline, service):
    request = LocalIdeaRequest(
        model_name="custom-model",
        temperature=0.8,
        top_p=0.95,
        repetition_penalty=1.3,
    )

    result = service.generate(request)

    assert result == expected_idea
    mock_pipeline.assert_called_once_with(
        "text-generation",
        model=request.model_name,
        torch_dtype=pytest.importorskip("torch").float16,
        device_map="auto",
    )
    mock_pipeline.return_value.assert_called_once_with(
        "mocked prompt",
        max_new_tokens=20,
        do_sample=True,
        temperature=request.temperature,
        top_p=request.top_p,
        repetition_penalty=request.repetition_penalty,
        pad_token_id=234,
        eos_token_id=234,
        return_full_text=False,
    )
    _assert_chat_template(mock_pipeline)


def _assert_chat_template(mock_pipeline):
    mock_pipeline.return_value.tokenizer.apply_chat_template.assert_called_once_with(
        LocalIdeaService.get_chat_template(),
        tokenize=False,
        add_generation_prompt=True,
    )

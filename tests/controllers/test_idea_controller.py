import pytest
from unittest.mock import Mock, patch
from controllers.idea_controller import IdeaController
from models.api import AbstractIdeaRequest, IdeaResponse
from services.local_idea_service import LocalIdeaService
from services.remote_idea_service import RemoteIdeaService
from services.service_mode import ServiceMode


@pytest.fixture
def svc_patches():
    with (
        patch("controllers.idea_controller.RemoteIdeaService") as mock_remote_svc,
        patch("controllers.idea_controller.LocalIdeaService") as mock_local_svc,
    ):
        mock_remote_svc.return_value = Mock(spec=RemoteIdeaService)
        mock_local_svc.return_value = Mock(spec=LocalIdeaService)

        yield {
            ServiceMode.REMOTE: mock_remote_svc,
            ServiceMode.LOCAL: mock_local_svc,
        }


@pytest.mark.parametrize(
    "svc_mode, expected_response",
    [
        (ServiceMode.REMOTE, "remote idea"),
        (ServiceMode.LOCAL, "local idea"),
    ],
)
def test_get_idea(svc_patches, svc_mode, expected_response):
    mock_svc = svc_patches[svc_mode].return_value
    mock_svc.generate.return_value = expected_response
    mock_request = Mock(spec=AbstractIdeaRequest)
    controller = IdeaController(svc_mode)

    response = controller.get_idea(mock_request)

    assert response.idea == expected_response
    mock_svc.generate.assert_called_once_with(mock_request)


@pytest.mark.parametrize(
    "svc_mode",
    [
        ServiceMode.REMOTE,
        ServiceMode.LOCAL,
    ],
)
def test_get_idea_when_service_returns_empty_then_return_none(svc_patches, svc_mode):
    mock_svc = svc_patches[svc_mode].return_value
    mock_svc.generate.return_value = ""
    mock_request = Mock(spec=AbstractIdeaRequest)
    controller = IdeaController(svc_mode)

    response = controller.get_idea(mock_request)

    assert response is None

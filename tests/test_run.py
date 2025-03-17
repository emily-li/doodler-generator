from flask import Response
import pytest
import json
import sys
import os
from unittest.mock import Mock
from models.api import IdeaResponse
from controllers.idea_controller import IdeaController
import routes
from run import app

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


@pytest.fixture
def controller():
    controller = Mock(spec=IdeaController)
    controller.get_idea.return_value = IdeaResponse(idea="mock response")
    return controller


@pytest.fixture
def client(controller):
    routes._controller = controller

    return app.test_client()


def test_ui_request_when_post_then_return_cors_headers(client):
    origins = {
        "http://localhost:5173": True,
        "https://emily-li.github.io": True,
        "https://something-else.woah.com": False,
    }
    for origin, allowed in origins.items():
        response = client.options("/api/v1/idea", headers={"Origin": origin})

        if allowed:
            assert response.status_code == 200
            assert "Access-Control-Allow-Origin" in response.headers
            assert response.headers["Access-Control-Allow-Origin"] == origin
        else:
            assert "Access-Control-Allow-Origin" not in response.headers


def test_idea_endpoint(client, controller):
    response: Response = client.post(
        "/api/v1/idea", json={}, headers={"Content-Type": "application/json"}
    )
    print(response.data)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["idea"] == controller.get_idea.return_value.idea

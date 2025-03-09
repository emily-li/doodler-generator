import pytest
import json
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from run import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


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


def test_idea_endpoint(client):
    response = client.post(
        "/api/v1/idea", json="{}", headers={"Content-Type": "application/json"}
    )
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["idea"] is not None

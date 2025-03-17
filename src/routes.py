from typing import Optional
from flask import Blueprint, request, Request
from flask.views import MethodView
from controllers.idea_controller import IdeaController
from dataclasses import asdict
from dacite import from_dict
from models.api import (
    AbstractIdeaRequest,
    IdeaResponse,
    LocalIdeaRequest,
    RemoteIdeaRequest,
)
from services.service_mode import ServiceMode
from dotenv import load_dotenv
import os


def _read_service_mode() -> ServiceMode:
    load_dotenv()
    service_mode = os.getenv("SERVER_MODE")
    return ServiceMode.from_string(service_mode)


_bp: Blueprint = Blueprint("api_v1", __name__)
_service_mode = _read_service_mode()
_controller: IdeaController


def setup_routes(app) -> None:
    global _controller
    _controller = IdeaController(_service_mode)
    view = IdeaView.as_view("idea_view")

    _bp.url_prefix = "/api/v1"
    _bp.add_url_rule("/idea", view_func=view, methods=["POST"])

    app.register_blueprint(_bp)


def _parse_request(service_mode: ServiceMode, request: Request) -> AbstractIdeaRequest:
    clz = RemoteIdeaRequest if service_mode == ServiceMode.REMOTE else LocalIdeaRequest
    return from_dict(data_class=clz, data=request.get_json() or {})


class IdeaView(MethodView):
    def post(self):
        idea_request: AbstractIdeaRequest = _parse_request(_service_mode, request)
        idea: Optional[IdeaResponse] = _controller.get_idea(idea_request)
        if idea:
            return asdict(idea), 200
        else:
            return "", 503

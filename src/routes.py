from flask import Blueprint, jsonify, request
from controllers.idea_controller import IdeaController
from dataclasses import asdict
from dacite import from_dict
from models.api import IdeaRequest

_bp: Blueprint = Blueprint("api_v1", __name__)
_idea_controller: IdeaController = IdeaController()


@_bp.route("/idea", methods=["POST"])
def get_idea() -> str:
    idea_request = from_dict(data_class=IdeaRequest, data=request.get_json() or {})

    idea = _idea_controller.get_idea(idea_request)

    return jsonify(asdict(idea))


# @bp.route('doodle', methods=['POST'])
# def get_doodle(idea: str):
#    return doodle_controller.get_doodle(idea)


def setup_routes(app) -> None:
    app.register_blueprint(_bp, url_prefix="/api/v1")

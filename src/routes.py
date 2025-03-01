from flask import Blueprint, jsonify
from controllers.idea_controller import IdeaController
from dataclasses import asdict

api_v1: Blueprint = Blueprint('api_v1', __name__)
idea_controller: IdeaController = IdeaController()

@api_v1.route('/idea', methods=['POST'])
def get_idea() -> str:
    idea = idea_controller.get_idea()
    return jsonify(asdict(idea))

# @bp.route('doodle', methods=['POST'])
# def get_doodle(idea: str):
#    return doodle_controller.get_doodle(idea)

def setup_routes(app) -> None:
    app.register_blueprint(api_v1, url_prefix='/api/v1')

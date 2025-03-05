from services.local_idea_service import LocalIdeaService
from services.abstract_idea_service import AbstractIdeaService
from models.api import IdeaRequest, IdeaResponse


class IdeaController:
    _idea_service: AbstractIdeaService

    def __init__(self):
        self._idea_service = LocalIdeaService()

    def get_idea(self, request: IdeaRequest) -> IdeaResponse:
        return IdeaResponse(self._idea_service.generate(request))

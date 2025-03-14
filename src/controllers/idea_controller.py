from typing import Optional
from services.local_idea_service import LocalIdeaService
from services.remote_idea_service import RemoteIdeaService
from services.abstract_idea_service import AbstractIdeaService
from models.api import AbstractIdeaRequest, IdeaResponse
from services.service_mode import ServiceMode


class IdeaController:

    def __init__(self, service_mode: ServiceMode):
        self._idea_service = self._build_service(service_mode)

    def get_idea(self, request: AbstractIdeaRequest) -> Optional[IdeaResponse]:
        idea = self._idea_service.generate(request)
        if len(idea):
            return IdeaResponse(idea)
        else:
            return None

    @staticmethod
    def _build_service(service_mode: ServiceMode) -> AbstractIdeaService:
        if service_mode == ServiceMode.REMOTE:
            service = RemoteIdeaService()
        else:
            service = LocalIdeaService()
        print(f" * Service running in mode: {service_mode.value}")
        return service

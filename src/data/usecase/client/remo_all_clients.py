from src.core.dto.client_dto import Client
from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RemoveAllClientsUC(UseCaseABC):
    def __init__(self, client_repo: ClientRepoABC):
        self.client_repo = client_repo

    def execute(self) -> None:
        self.client_repo.remove_all()

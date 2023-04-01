from src.core.dto.client_dto import Client
from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RegisterNewClientUC(UseCaseABC):
    def __init__(self, client_repo: ClientRepoABC, client: Client):
        self.client_repo = client_repo
        self.client = client

    def execute(self):
        self.client_repo.add(self.client)
        
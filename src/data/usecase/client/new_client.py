from src.core.dto.client_dto import Client
from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RegisterNewClientUC(UseCaseABC):
    def __init__(self, client_repo: ClientRepoABC):
        self.client_repo = client_repo

    def execute(self, client: Client) -> None:
        if self.client_repo.find_by_passport(client.passport_number) is not None:
            raise ValueError('Клиент уже существует')
        self.client_repo.add(client)

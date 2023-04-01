from src.core.repo.usecase.usecaseABC import UseCaseABC


class RegisterNewClientUC(UseCaseABC):
    def __init__(self, client_repo, client):
        self.client_repo = client_repo
        self.client = client

    def execute(self):
        self.client_repo.add(self.client)
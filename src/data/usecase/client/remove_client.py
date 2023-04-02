from src.core.dto.client_dto import Client
from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RemoveClientUC(UseCaseABC):
    def __init__(self, client_repo: ClientRepoABC, sim_repo: SimRepoABC):
        self.client_repo = client_repo
        self.sim_repo = sim_repo

    def execute(self, client: Client):
        self.client_repo.remove(client)


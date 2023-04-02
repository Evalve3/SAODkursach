from src.core.dto.client_dto import Client
from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class ClientBySimNumber(UseCaseABC):
    def __init__(self, sim_clients_repo: ClientSimsABC, client_repo: ClientRepoABC) -> None:
        self.sim_clients_repo = sim_clients_repo
        self.client_repo = client_repo

    def execute(self, sim_number: str) -> Client:
        sim = self.sim_clients_repo.find_by_sim_number(sim_number)
        client = self.client_repo.find_by_passport(sim.passport_number)
        return client

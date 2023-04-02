from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RegisterSimNumber(UseCaseABC):
    def __init__(self, sim_clients_repo: ClientSimsABC, sim_repo: SimRepoABC) -> None:
        self.sim_clients_repo = sim_clients_repo
        self.sim_repo = sim_repo

    def execute(self, client: Client, sim: Sim, date_end: str) -> bool:
        if not sim.has:
            return False
        self.sim_clients_repo.register_sim_number(client, sim, date_end)
        sim.has = False
        return True

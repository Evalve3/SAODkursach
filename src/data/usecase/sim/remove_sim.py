from src.core.dto.sim_dto import Sim
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RemoveSimUC(UseCaseABC):
    def __init__(self, sim_repo: SimRepoABC, sim_client_repo: ClientSimsABC) -> None:
        self.sim_repo = sim_repo
        self.sim_clients_repo = sim_client_repo

    def execute(self, sim: Sim) -> bool:
        try:
            self.sim_clients_repo.find_by_sim_number(sim.sim_number)
            return False
        except ValueError:
            self.sim_repo.remove(sim)
            return True

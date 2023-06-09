from src.core.dto.sim_dto import Sim
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RegisterSimReturnNumber(UseCaseABC):
    def __init__(self, sim_clients_repo: ClientSimsABC, sim_repo: SimRepoABC) -> None:
        self.sim_clients_repo = sim_clients_repo
        self.sim_repo = sim_repo

    def execute(self, sim: Sim) -> bool:
        self.sim_clients_repo.remove_sim(sim)
        self.sim_repo.edit_sim(sim, {'has': True})
        return True

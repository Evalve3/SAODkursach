from src.core.dto.sim_dto import Sim
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class AddNewSimUC(UseCaseABC):
    def __init__(self, sim_repo: SimRepoABC):
        self.sim_repo = sim_repo

    def execute(self, sim: Sim) -> None:
        return self.sim_repo.add(sim)

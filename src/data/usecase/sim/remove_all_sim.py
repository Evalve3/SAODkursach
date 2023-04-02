from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RemoveAllSimUC(UseCaseABC):
    def __init__(self, sim_repo: SimRepoABC):
        self.sim_repo = sim_repo

    def execute(self) -> None:
        return self.sim_repo.remove_all()

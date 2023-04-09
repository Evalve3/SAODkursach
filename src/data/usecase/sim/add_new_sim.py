from src.core.dto.sim_dto import Sim
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class AddNewSimUC(UseCaseABC):
    def __init__(self, sim_repo: SimRepoABC):
        self.sim_repo = sim_repo

    def execute(self, sim: Sim) -> None:
        if self.sim_repo.find_by_number(sim.sim_number) is not None:
            raise ValueError("Симкарта с таким номером уже существует")
        return self.sim_repo.add(sim)

from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RemoveAllSimUC(UseCaseABC):
    def __init__(self, sim_repo: SimRepoABC, sim_client_repo: ClientSimsABC):
        self.sim_repo = sim_repo
        self.sim_client_repo = sim_client_repo

    def execute(self) -> None:
        all_sims = self.sim_repo.get_all()
        for sim in all_sims:
            try:
                self.sim_client_repo.remove_sim(sim)
            except Exception:
                continue
        return self.sim_repo.remove_all()


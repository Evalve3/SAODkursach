from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class RemoveAllClientsUC(UseCaseABC):
    def __init__(self, client_repo: ClientRepoABC, client_sims_repo: ClientSimsABC, sim_repo: SimRepoABC) -> None:
        self.client_repo = client_repo
        self.client_sims_repo = client_sims_repo
        self.sim_repo = sim_repo

    def execute(self) -> None:
        clients = self.client_repo.get_all()
        for client in clients:
            sims = self.client_sims_repo.find_client_sims(client)
            for sim_issue in sims:
                sim = self.sim_repo.find_by_number(sim_issue.sim_number)
                self.sim_repo.edit_sim(sim, {'has': True})
                self.client_sims_repo.remove_sim(sim)
        self.client_repo.remove_all()

from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.presenterABC import PresenterABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class ClientBySimNumber(UseCaseABC):
    def __init__(self, sim_clients_repo: ClientSimsABC, client_repo: ClientRepoABC, presenter: PresenterABC, sim_repo: SimRepoABC) -> None:
        self.sim_clients_repo = sim_clients_repo
        self.client_repo = client_repo
        self.presenter = presenter
        self.sim_repo = sim_repo

    def execute(self, sim_number: str) -> dict:
        try:
            sim_issue = self.sim_clients_repo.find_by_sim_number(sim_number)
        except ValueError:
            return self.sim_repo.find_by_number(sim_number).__dict__
        sim = self.sim_repo.find_by_number(sim_number)
        client = self.client_repo.find_by_passport(sim_issue.passport_number)
        ans = self.presenter.present(response=(client, sim))
        return ans

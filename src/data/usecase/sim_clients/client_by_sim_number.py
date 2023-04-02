from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.usecase.presenterABC import PresenterABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class ClientBySimNumber(UseCaseABC):
    def __init__(self, sim_clients_repo: ClientSimsABC, client_repo: ClientRepoABC, presenter: PresenterABC) -> None:
        self.sim_clients_repo = sim_clients_repo
        self.client_repo = client_repo
        self.presenter = presenter

    def execute(self, sim_number: str) -> dict:
        sim = self.sim_clients_repo.find_by_sim_number(sim_number)
        client = self.client_repo.find_by_passport(sim.passport_number)
        ans = self.presenter.present(response=(client, sim))
        return ans

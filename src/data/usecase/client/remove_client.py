from src.core.dto.client_dto import Client
from src.core.repo.client.client_repo import ClientRepoABC
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC
from src.core.repo.usecase.usecaseABC import UseCaseABC
from src.data.sim_repo.sim_repo import SimRepo


class RemoveClientUC(UseCaseABC):
    def __init__(self, client_repo: ClientRepoABC, sim_client_repo: ClientSimsABC, sim_repo: SimRepo) -> None:
        self.client_repo = client_repo
        self.sim_client_repo = sim_client_repo
        self.sim_repo = sim_repo

    def execute(self, client: Client) -> None:
        sims = self.sim_client_repo.find_client_sims(client)
        for sim in sims:
            sim_dto = self.sim_repo.find_by_number(sim.sim_number)
            self.sim_repo.edit_sim(sim_dto, {'has': True})
            self.sim_client_repo.remove_sim(sim_dto)
        if self.client_repo.find_by_passport(client.passport_number) is None:
            raise ValueError("Клиент не найден")
        self.client_repo.remove(client)


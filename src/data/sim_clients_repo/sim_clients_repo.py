from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.dto.sim_return_dto import SimIssueRefund
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC


class SimClientIssueRefundRepo(ClientSimsABC):
    def find_by_sim_number(self, sim_number: str) -> SimIssueRefund:
        for i in range(len(self.sim_list)):
            sim = self.sim_list[i]
            if sim.sim_number == sim_number:
                return sim
        raise ValueError("Sim not found")

    def find_client_sims(self, client: Client) -> list[SimIssueRefund]:
        ans = []
        for i in range(len(self.sim_list)):
            sim = self.sim_list[i]
            if sim.passport_number == client.passport_number:
                ans.append(sim)
        return ans

    def register_sim_number(self, client: Client, sim: Sim) -> None:
        pass

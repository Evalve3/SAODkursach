import datetime

from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.dto.sim_return_dto import SimIssueRefund
from src.core.repo.client_sims_repo.sim_clients_repo import ClientSimsABC


class SimClientIssueRefundRepo(ClientSimsABC):
    def find_by_sim_number(self, sim_number: str) -> SimIssueRefund:
        for sim in self.sim_list:
            if sim.sim_number == sim_number:
                return sim
        raise ValueError("Sim not found")

    def find_client_sims(self, client: Client) -> list[SimIssueRefund]:
        ans = []
        for sim in self.sim_list:
            if sim.passport_number == client.passport_number:
                ans.append(sim)
        return ans

    def register_sim_number(self, client: Client, sim: Sim, date_end: str) -> None:
        self.sim_list.add_tail(
            SimIssueRefund(sim_number=sim.sim_number, passport_number=client.passport_number, date_end=date_end,
                           date_of_issue=str(datetime.date.today())))

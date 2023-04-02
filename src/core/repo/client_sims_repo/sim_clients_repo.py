from abc import ABCMeta, abstractmethod

from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.dto.sim_return_dto import SimIssueRefund
from src.core.repo.data_structures.my_list.my_list_repo import ListABC


class ClientSimsABC(metaclass=ABCMeta):
    def __init__(self, lst: ListABC) -> None:
        self.sim_list = lst

    @abstractmethod
    def find_client_sims(self, client: Client) -> list[SimIssueRefund]:
        pass

    @abstractmethod
    def find_by_sim_number(self, sim_number: str) -> SimIssueRefund:
        pass

    @abstractmethod
    def register_sim_number(self, client: Client, sim: Sim) -> None:
        pass

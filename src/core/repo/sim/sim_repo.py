from abc import abstractmethod, ABCMeta

from src.core.dto.sim_dto import Sim
from src.core.repo.hash_table.hash_table_repo import HashTableABC


class SimRepoABC(metaclass=ABCMeta):
    def __init__(self, hash_table: HashTableABC):
        self.sim_list = hash_table

    @abstractmethod
    def add(self, sim: Sim) -> None:
        pass

    @abstractmethod
    def remove(self, sim: Sim) -> None:
        pass

    @abstractmethod
    def find_by_number(self, number: str) -> Sim:
        pass

    @abstractmethod
    def get_all(self) -> list[Sim]:
        pass

    @abstractmethod
    def clear_data(self, sim: Sim) -> None:
        pass

    @abstractmethod
    def find_by_tariff(self, tariff: str) -> list[Sim]:
        pass

from abc import abstractmethod, ABCMeta

from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.dto.sim_return_dto import SimIssueRefund
from src.core.repo.algorithms.search_in_text.search_text_repo import SearchInTextABC
from src.core.repo.data_structures.tree.tree_repo import TreeABC


class ClientRepoABC(metaclass=ABCMeta):

    def __init__(self, tree: TreeABC, search_in_text: SearchInTextABC) -> None:
        self.client_tree = tree
        self.search_in_text = search_in_text

    @abstractmethod
    def add(self, client: Client) -> None:
        pass

    @abstractmethod
    def remove(self, client: Client) -> None:
        pass

    @abstractmethod
    def find_by_passport(self, passport: str) -> Client:
        pass

    @abstractmethod
    def get_all(self) -> list[Client]:
        pass

    @abstractmethod
    def remove_all(self) -> None:
        pass

    @abstractmethod
    def find_by_text(self, text: str) -> list[Client]:
        pass


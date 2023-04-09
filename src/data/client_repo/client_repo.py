from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.dto.sim_return_dto import SimIssueRefund
from src.core.repo.client.client_repo import ClientRepoABC


class ClientRepo(ClientRepoABC):
    """    def __init__(self, tree: TreeABC, search_int_text: SearchInTextABC) -> None:
        self.client_tree = tree
        self.search_in_text = search_int_text
        """

    def remove_all(self) -> None:
        self.client_tree.remove_all()

    def add(self, client: Client) -> None:
        self.client_tree.insert(client.passport_number, client)

    def remove(self, client: Client) -> None:
        self.client_tree.remove(client.passport_number)

    def find_by_passport(self, passport: str) -> Client:
        return self.client_tree.find(passport).data if self.client_tree.find(passport) is not None else None

    def get_all(self) -> list[Client]:
        return [node.data for node in self.client_tree.get_all()]

    def find_by_text(self, text: str) -> list[Client]:
        search_func = self.search_in_text.search
        # print(self.client_tree.get_all())
        return [node.data for node in self.client_tree.get_all() if
                search_func(node.data.full_name, text) or search_func(node.data.address, text)]

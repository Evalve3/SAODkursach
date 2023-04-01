from src.core.dto.sim_dto import Sim
from src.core.repo.sim.sim_repo import SimRepoABC


class SimRepo(SimRepoABC):

    def add(self, sim: Sim) -> None:
        self.sim_list.insert(sim.sim_number, sim)

    def remove(self, sim: Sim) -> None:
        self.sim_list.remove(sim.sim_number)

    def find_by_number(self, number: str) -> Sim:
        return self.sim_list.find(number).data

    def get_all(self) -> list[Sim]:
        return [node.data for node in self.sim_list.get_all()]

    def clear_data(self, sim: Sim) -> None:
        pass

    def find_by_tariff(self, tariff: str) -> list[Sim]:
        pass


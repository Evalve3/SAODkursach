from src.core.dto.sim_dto import Sim
from src.core.repo.sim.sim_repo import SimRepoABC


class SimRepo(SimRepoABC):

    def edit_sim(self, sim: Sim, data: dict) -> None:
        self.sim_list.edit_data(sim.sim_number, data)

    def add(self, sim: Sim) -> None:
        self.sim_list.insert(sim.sim_number, sim)

    def remove(self, sim: Sim) -> None:
        self.sim_list.remove(sim.sim_number)

    def find_by_number(self, number: str) -> Sim:
        return self.sim_list.find(number) if not isinstance(self.sim_list.find(number), int) else None

    def get_all(self) -> list[Sim]:
        return [node.data for node in self.sim_list.get_all()]

    def remove_all(self) -> None:
        self.sim_list.remove_all()

    def find_by_tariff(self, tariff: str) -> list[Sim]:
        return [node.data for node in self.sim_list.get_all() if node.data.tariff_plan == tariff]





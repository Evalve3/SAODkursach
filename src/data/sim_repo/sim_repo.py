from src.core.dto.sim_dto import Sim
from src.core.repo.sim.sim_repo import SimRepoABC


class SimRepo(SimRepoABC):

    def add(self, sim: Sim) -> None:
        self.sim_list.insert(sim.sim_number, sim)

    def remove(self, sim: Sim) -> None:
        self.sim_list.remove(sim.sim_number)

    def find_by_number(self, number: str) -> Sim:
        return self.sim_list.find(number)

    def get_all(self) -> list[Sim]:
        return [node.data for node in self.sim_list.get_all()]

    def remove_all(self) -> None:
        self.sim_list.remove_all()

    def find_by_tariff(self, tariff: str) -> list[Sim]:
        return [node.data for node in self.sim_list.get_all() if node.data.tariff_plan == tariff]

    def edit_sim(self, sim: Sim) -> None:
        sim_in_list = self.sim_list.find(sim.sim_number)
        sim_in_list.tariff_plan = sim.tariff_plan
        sim_in_list.year_of_issue = sim.year_of_issue



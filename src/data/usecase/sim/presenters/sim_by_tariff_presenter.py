from src.core.dto.sim_dto import Sim
from src.core.repo.usecase.presenterABC import PresenterABC


class SimByTariffPresenter(PresenterABC):

    def present(self, response: list[Sim]):
        # номер, тариф, год выпуска
        ans = [{'number': r.sim_number, 'tariff': r.tariff_plan, 'year': r.year_of_issue} for r in response]
        return ans

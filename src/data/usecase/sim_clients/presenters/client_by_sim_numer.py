from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.repo.usecase.presenterABC import PresenterABC


class SimByClientfPresenter(PresenterABC):

    def present(self, response: (Sim, Client)):
        # номер, тариф, год выпуска, активность, имя, паспорт
        sim = response[0]
        client = response[1]
        ans = {'number': sim.sim_number, 'tariff': sim.tariff_plan, 'year': sim.year_of_issue, 'has': sim.has,
               'name': client.full_name, 'passport': client.passport_number}
        return ans

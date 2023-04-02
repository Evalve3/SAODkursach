from src.core.repo.sim.sim_repo import SimRepoABC
from src.core.repo.usecase.presenterABC import PresenterABC
from src.core.repo.usecase.usecaseABC import UseCaseABC


class FindSimByTariffUC(UseCaseABC):
    def __init__(self, sim_repo: SimRepoABC, presenter: PresenterABC):
        self.sim_repo = sim_repo
        self.presenter = presenter

    def execute(self, tariff: str) -> list[dict]:
        # номер, тариф, год выпуска
        ans = self.sim_repo.find_by_tariff(tariff)
        return self.presenter.present(response=ans)

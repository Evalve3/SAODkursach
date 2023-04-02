from dataclasses import dataclass
import re

@dataclass
class Sim:
    sim_number: str
    tariff_plan: str
    year_of_issue: int
    active: bool

    def __eq__(self, other):
        return self.sim_number == other.sim_number

    def __lt__(self, other):
        return self.sim_number < other.sim_number

    def __gt__(self, other):
        return self.sim_number > other.sim_number

    def __le__(self, other):
        return self.sim_number <= other.sim_number

    def __ge__(self, other):
        return self.sim_number >= other.sim_number

    def __post_init__(self):
        self._validate_sim_number()
        self._validate_tariff_plan()
        self._validate_year_of_issue()
        self._validate_active()

    def _validate_sim_number(self) -> None:
        if not isinstance(self.sim_number, str):
            raise TypeError('Invalid type of sim number')
        regex = re.compile(r"^[0-9]{3}-[0-9]{7}$")
        if not bool(regex.match(self.sim_number)):
            raise ValueError('Invalid sim number')

    def _validate_tariff_plan(self) -> None:
        if not isinstance(self.tariff_plan, str):
            raise TypeError('Invalid type of tariff plan')
        if len(self.tariff_plan) > 100:
            raise ValueError('Invalid tariff plan')

    def _validate_year_of_issue(self) -> None:
        if not isinstance(self.year_of_issue, int):
            raise TypeError('Invalid type of year of issue')
        if self.year_of_issue < 1900 or self.year_of_issue > 2023:
            raise ValueError('Invalid year of issue')

    def _validate_active(self) -> None:
        if not isinstance(self.active, bool):
            raise TypeError('Invalid type of active')
        if self.active not in (True, False):
            raise ValueError('Invalid active')

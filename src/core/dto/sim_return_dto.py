import re
from dataclasses import dataclass


@dataclass
class SimIssueRefund:
    passport_number: str
    sim_number: str
    date_of_issue: str
    date_end: str

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
        self._validate_passport_number()
        self._validate_sim_number()
        self._validate_date_of_issue()
        self._validate_date_end()

    def _validate_passport_number(self) -> None:
        if not isinstance(self.passport_number, str):
            raise TypeError('Invalid type of passport number')
        regex = re.compile(r"^[0-9]{4}-[0-9]{6}$")
        if not bool(regex.match(self.passport_number)):
            raise ValueError('Invalid passport number')

    def _validate_sim_number(self) -> None:
        if not isinstance(self.sim_number, str):
            raise TypeError('Invalid type of sim number')
        regex = re.compile(r"^[0-9]{3}-[0-9]{7}$")
        if not bool(regex.match(self.sim_number)):
            raise ValueError('Invalid sim number')

    def _validate_date_of_issue(self) -> None:
        if not isinstance(self.date_of_issue, str):
            raise TypeError('Invalid type of date of issue')
        if len(self.date_of_issue) > 100:
            raise ValueError('Invalid date of issue')

    def _validate_date_end(self) -> None:
        if not isinstance(self.date_end, str):
            raise TypeError('Invalid type of date end')
        if len(self.date_end) > 100:
            raise ValueError('Invalid date end')

from dataclasses import dataclass
import re


@dataclass
class Client:
    passport_number: str
    place_date_of_issue: str
    full_name: str
    year_of_birth: int
    address: str

    def __post_init__(self):
        self._validate_passport_number()
        self._validate_place_date_of_issue()
        self._validate_full_name()
        self._validate_year_of_birth()
        self._validate_address()

    def _validate_address(self) -> None:
        if not isinstance(self.address, str):
            raise TypeError('Invalid type of address')

        if len(self.address) > 100:
            raise ValueError('Invalid address')

    def _validate_year_of_birth(self) -> None:
        if not isinstance(self.year_of_birth, int):
            raise TypeError('Invalid type of year of birth')
        if self.year_of_birth < 1900 or self.year_of_birth > 2023:
            raise ValueError('Invalid year of birth')

    def _validate_full_name(self) -> None:
        if not isinstance(self.full_name, str):
            raise TypeError('Invalid type of full name')
        if len(self.full_name) > 100:
            raise ValueError('Invalid full name')

    def _validate_place_date_of_issue(self) -> None:
        if not isinstance(self.place_date_of_issue, str):
            raise TypeError('Invalid type of place date of issue')
        if len(self.place_date_of_issue) > 100:
            raise ValueError('Invalid place date of issue')

    def _validate_passport_number(self) -> None:
        if not isinstance(self.passport_number, str):
            raise TypeError('Invalid type of passport number')
        regex = re.compile(r"^[0-9]{4}-[0-9]{6}$")
        if not bool(regex.match(self.passport_number)):
            raise ValueError('Invalid passport number')

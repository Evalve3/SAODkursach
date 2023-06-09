from abc import abstractmethod, ABCMeta
from typing import Any


class Elem:
    def __init__(self):
        self.key = ''
        self.data = None
        self.deleted = False


class HashTableABC(metaclass=ABCMeta):

    def __init__(self, table_len):
        self.dict = [Elem() for _ in range(table_len)]
        self.table_len = table_len

    @abstractmethod
    def hash(self, key: str) -> int:
        pass

    @abstractmethod
    def insert(self, key: str, data: Any) -> None:
        pass

    @abstractmethod
    def remove(self, key: str) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def find(self, key: str) -> Any:
        pass

    @abstractmethod
    def edit_data(self, key: str, data: dict) -> None:
        pass

    @abstractmethod
    def remove_all(self) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[Elem]:
        pass

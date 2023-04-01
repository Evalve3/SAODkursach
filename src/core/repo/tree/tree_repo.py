from dataclasses import dataclass
from typing import Optional, Any
from abc import abstractmethod, ABCMeta

@dataclass
class Node:
    key: str
    data: Any
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    height: int = 1

    def __repr__(self):
        return f'<Node "{self.data}">'


class TreeABC(metaclass=ABCMeta):
    def __init__(self):
        self.root = None

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
    def find(self, key: str) -> Optional[Node]:
        pass

    @abstractmethod
    def get_all(self) -> list[Node]:
        pass

    @abstractmethod
    def clear_data(self, key: str) -> None:
        pass

from dataclasses import dataclass
from typing import Optional
from abc import abstractmethod, ABCMeta

@dataclass
class Node:
    key: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    height: int = 1

    def __repr__(self):
        return f'<Node "{self.key}">'


class TreeABC(metaclass=ABCMeta):
    def __init__(self):
        self.root = None

    @abstractmethod
    def insert(self, key: int) -> None:
        pass

    @abstractmethod
    def remove(self, key: int) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def find(self, key: int) -> bool:
        pass


from abc import ABCMeta, abstractmethod


class Elem:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class ListABC(metaclass=ABCMeta):
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    @abstractmethod
    def add_tail(self, value: int) -> None:
        pass

    @abstractmethod
    def remove(self, position: int) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def get_elem(self, position: int) -> Elem:
        pass

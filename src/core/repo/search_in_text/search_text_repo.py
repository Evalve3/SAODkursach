from abc import abstractmethod, ABCMeta


class SearchInTextABC(metaclass=ABCMeta):

    @abstractmethod
    def search(self, text, pattern) -> bool:
        pass

from abc import abstractmethod, ABCMeta


class UseCaseABC(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
    
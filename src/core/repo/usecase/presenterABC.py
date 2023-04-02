from abc import ABCMeta, abstractmethod


class PresenterABC(metaclass=ABCMeta):

    @abstractmethod
    def present(self, response: any):
        pass

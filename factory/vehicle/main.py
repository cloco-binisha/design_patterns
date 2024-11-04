from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

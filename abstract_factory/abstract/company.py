from abc import ABC, abstractmethod

from .gpu import Gpu
from .monitor import Monitor


class CompanyFactory(ABC):
    @abstractmethod
    def createGpu(self) -> Gpu:
        pass

    @abstractmethod
    def createMonitor(self) -> Monitor:
        pass
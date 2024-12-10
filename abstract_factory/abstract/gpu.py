from abc import ABC, abstractmethod



class Gpu(ABC):
    @abstractmethod
    def assemble(self):
        pass
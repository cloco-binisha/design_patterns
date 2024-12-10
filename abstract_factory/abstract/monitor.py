from abc import ABC, abstractmethod



class Monitor(ABC):
    @abstractmethod
    def assemble(self):
        pass
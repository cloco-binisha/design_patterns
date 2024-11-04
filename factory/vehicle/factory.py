from abc import ABC, abstractmethod

from vehicle.main import Vehicle


class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass
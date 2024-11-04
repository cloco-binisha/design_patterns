from car.main import Car
from vehicle.factory import VehicleFactory
from vehicle.main import Vehicle


class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()


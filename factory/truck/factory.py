from truck.main import Truck
from vehicle.factory import VehicleFactory
from vehicle.main import Vehicle


class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()

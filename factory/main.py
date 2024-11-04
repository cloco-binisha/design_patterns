
from car.factory import CarFactory
from truck.factory import TruckFactory


if __name__ == "__main__":
    car_factory = CarFactory()
    truck_factory = TruckFactory()

    car = car_factory.createVehicle()
    truck = truck_factory.createVehicle()

    print(car.getType())
    print(truck.getType())  
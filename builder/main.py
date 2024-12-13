from .car_builder import CarBuilder


if __name__ == "__main__":
    car = (CarBuilder('Tesla', 'Model S')
        .set_year(2024)
        .set_color('Red')
        .add_gps()
        .build())

    print(car.describe())
from .car import Car


class CarBuilder:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.year = None
        self.color = None
        self.hasGPS = False
        self.hasSunroof = False

    def set_year(self, year):
        self.year = year
        return self

    def set_color(self, color):
        self.color = color
        return self

    def add_gps(self):
        self.hasGPS = True
        return self

    def add_sunroof(self):
        self.hasSunroof = True
        return self

    def build(self):
        return Car(self)

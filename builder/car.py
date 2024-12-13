class Car:
    def __init__(self, builder):
        self.make = builder.make
        self.model = builder.model
        self.year = builder.year
        self.color = builder.color
        self.hasGPS = builder.hasGPS
        self.hasSunroof = builder.hasSunroof

    def describe(self):
        return f"{self.year} {self.make} {self.model} in {self.color} color with GPS: {self.hasGPS} and Sunroof: {self.hasSunroof}"


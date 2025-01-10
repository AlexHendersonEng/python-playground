# Define a car class
class Car:
    # Car attributes
    make = None
    model = None
    year = None
    colour = None

    # Car construtor
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    # Car methods
    def drive(self):
        print("This " + self.make + " " + self.model + " car is driving")

    def stop(self):
        print("This " + self.make + " " + self.model + " car is stopped")

# Construct car objects
car_1 = Car("Vauxhall", "Corsa", "2001", "blue")
car_2 = Car("Audi", "A1", "2010", "red")

# Call car objects methods
car_1.drive()
car_2.stop()
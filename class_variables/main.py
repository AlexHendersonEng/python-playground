# Class variable: A class variable is declared directly within the class
#                 outside of any methods. Class variables are typically
#                 used for data that should be common to all instances, like
#                 constants or shared states.

# Instance variable: An instance variable is initialised inside a method of
#                    the class using self. Instance variables are typically 
#                    used for data unique to each object.

# Instance variable: 

# Define car class
class Car:
    wheels = 4 # Class variable

    def __init__(self, make, model, year, colour):
        self.make = make # Instance variable
        self.model = model # Instance variable
        self.year = year # Instance variable
        self.colour = colour # Instance variable

# Print out car class variable value without constructing car object
print("Car class wheels class variable: " + str(Car.wheels))

# Change car class variable
Car.wheels = 2
print("Car class wheels class variable: " + str(Car.wheels))

# Construct car objects
car_1 = Car("Vauxhall", "Corsa", "2001", "blue")
car_2 = Car("Audi", "A1", "2010", "red")

# Modify car 1 objects wheels class variable
car_1.wheels = 4
print("Car 1 has " + str(car_1.wheels) + " wheels")
print("Car 2 has " + str(car_2.wheels) + " wheels")

# Print out car objects instance variables
print("Car 1 is a " + car_1.year + " " + car_1.colour + " " + car_1.make + " " + car_1.model)
print("Car 2 is a " + car_2.year + " " + car_2.colour + " " + car_2.make + " " + car_2.model)
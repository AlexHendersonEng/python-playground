# Abstract class: A class which contains one or more abstract methods

# Abstract method: A method that has a declaration but does not have an implementation

# Import abstract base class module
from abc import ABC, abstractmethod

class Vehicle(ABC):

    # Make the method an abstract method
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):

    # Define implementation for the superclass abstract method
    def go(self):
        print("Car is being driven")

class Motorcycle(Vehicle):

    # Define implementation for the superclass abstract method
    def go(self):
        print("Motorcycle is being driven")

# Construct objects
car = Car()
motorcycle = Motorcycle()

# Call methods
car.go()
motorcycle.go()
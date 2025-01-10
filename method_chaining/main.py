class Car:

    def turn_on(self):
        print("Engine on")

        # Return object to allow for method chaining
        return self

    def drive(self):
        print("Car moving")

        # Return object to allow for method chaining
        return self

    def brake(self):
        print("Car stopping")

        # Return object to allow for method chaining
        return self

    def turn_off(self):
        print("Engine off")

        # Return object to allow for method chaining
        return self

# Create car object
car = Car()

# Chain methods ('\' is used for line continuation)
car.turn_on().\
    drive().\
    brake().\
    turn_off()
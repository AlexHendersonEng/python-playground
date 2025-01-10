class Animal():

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    # Override eat method defined in superclass
    def eat(self):
        print("This rabbit is eating")

# Construct object
rabbit = Rabbit()

# Call overridden method
rabbit.eat()
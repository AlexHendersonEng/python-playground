# Define great-grandparent superclass
class Organism:

    alive = True

# Define grandparent subclass
class Animal(Organism):

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This amimal is sleeping")

# Define parent subclasses
class Mammal(Animal):
    
    def run(self):
        print("This mammal is running")

class Fish(Animal):
    
    def swim(self):
        print("This fish is swimming")

class Bird(Animal):
    
    def fly(self):
        print("This bird is flying")

# Define child subclass using multiple inheritance
class Creature(Mammal, Fish, Bird):
    pass

# Construct objects
mammal = Mammal()
fish = Fish()
bird = Bird()
creature = Creature()

# Use methods defined in subclasses
mammal.run()
fish.swim()
bird.fly()

# Access attributes/methods on subclasses inherited from the parent classes
print("The mammal is " + "alive" if mammal.alive else "dead")
print("Bird: ", end="")
bird.eat()
print("Creature: ", end="")
creature.run()
print("Creature: ", end="")
creature.fly()

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        # The super function is used to obtain a temporary
        # copy of the superclass object
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        # The super function is used to obtain a temporary
        # copy of the superclass object
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

# Construct objects
square = Square(3, 4)
cube = Cube(3, 4, 5)

# Print area and volume
print("The area of the square is: " + str(square.area()))
print("The volume of the cube is: " + str(cube.volume()))
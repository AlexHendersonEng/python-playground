# Define Value class
class Value:

    # Constructor
    def __init__(self, val):
        self.value = val

    # Overload the '+' operator
    def __add__(self, other):
        return Value(self.value + other.value)

    # Override default __str__ method for how object is represented as a string
    def __str__(self):
        return str(self.value)

# Construct Value objects
a = Value(2)
b = Value(3)

# Use '+' operator
c = a + b

# Print resulting Value object
print(c)
# Walrus operator: Allows for the assignment of values to variables as
#                  part of a larger expression

# Build up list of foods from user input
foods = list()
while (food := input("Name a food or 'quit': ")) != "quit":
    foods.append(food)

# Print foods
print(foods)
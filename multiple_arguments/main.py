# Define a function with a varying amount of positional arguments
def add(*args):
    # The args is a tuple of the arguments passed to the function.
    # Print and return the sum of the arguments
    res = sum(args)
    print("The sum of the arguments is:", res)
    return res

# Define a function with a varying amount of keyword arguments
def multiply(**kwargs):
    # The kwargs is a dictionary of the arguments passed to the function.
    # Print and return the product of the arguments
    res = 1
    for key, value in kwargs.items():
        res *= value
    print("The product of the arguments is:", res)
    return res

# Call both functions
add(1, 2, 3)
multiply(a=1, b=2, c=3)

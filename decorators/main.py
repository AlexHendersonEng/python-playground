# Decorator: A function that takes another function as an argument and returns
#            a new function with enhanced functionality.

# Define basic decorator function
def decorator(func):

    def wrapper():
        print("Pre-function call")
        func()
        print("Post-function call")

    return wrapper

# Apply basic decorator to function
@decorator # Equivalent to 'hello = decorator(hello)'
def hello():
    print("Hello World!")

# Call function
print("Basic decorator:")
hello()
print()

# Define decorator function where decorator and function take arguments
def decorator1(message):

    def inner(func):

        def wrapper(*args, **kwargs):
            print(message)
            print("Pre-function call")
            func(*args, **kwargs)
            print("Post-function call")

        return wrapper

    return inner

# Apply decorator to function
@decorator1("Decorator function") # Equivalent to 'print_list = (decorator1(message))(print_list)'
def print_list(items):
    for item in items:
        print(item)

# Call function
print("Decorator function where decorator and decorated function take arguments:")
print_list(["One", "Two", "Three"])
print()

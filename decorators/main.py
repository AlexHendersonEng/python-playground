# Decorator: A function that takes another function as an argument and returns
#            a new function with enhanced functionality. Decorators often use the
#            shorthand '@' syntax as a shorthand for 'func = decorator(func)'.

# Define decorator function
def decorator(func):

    def wrapper():
        print("Pre-function call")
        func()
        print("Post-function call")

    return wrapper

# Apply decorator to function
@decorator
def hello():
    print("Hello World!")

# Call hello function
hello()
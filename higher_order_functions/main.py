# Higher order functions: A function that either accepts a function as an argument
#                         or returns a function.

# Define general function
def loud(text):
    return text.upper()

# Define higher order function that accepts a function as an argument
def hello(func):
    text = func("Hello")
    print(text)

# Define a higher order function that returns a function
def bye():
    def say_bye():
        print("Bye")

    return say_bye

# Call higher order functions
hello(loud)
say_bye = bye()
say_bye()
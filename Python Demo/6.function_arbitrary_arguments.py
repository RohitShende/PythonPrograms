""" Sometimes, we do not know in advance the number of arguments that will be
passed into a function. Python allows us to handle this kind of situation
through function calls with arbitrary number of arguments."""


def greet(*names):
    """This function greets all
   the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John", "rohit")

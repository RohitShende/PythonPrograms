def my_fun():
    pass


def my_fun_print():
    print("Welcome to my function")


def fun_with_parameters(a, b):
    print(a, b)


def fun_with_default_values(a, b=1):
    """ These are called default arguments """
    print(a, b)


my_fun()    # Calling a function

my_fun_print()

fun_with_parameters(1.3, 2.2)
fun_with_parameters("hello", 1)   # heterogeneous arguments, accepts whatever is sent

fun_with_default_values(5, 4)
fun_with_default_values(6)

fun_with_parameters(4, b=5)    # keyword arguments
fun_with_parameters(a=6, b="bye")




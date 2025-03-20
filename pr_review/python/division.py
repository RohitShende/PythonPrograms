"""
Program to divide a number `a` by `b` until it becomes 1 and count the number of
division operations it takes
"""


def divide_until_one(a, b):
    """
    Repeatedly divides an integer by a divisor until it becomes one.
    
    This function repeatedly applies integer division on the given number until the result 
    reaches one, incrementing a counter for each division performed. It assumes that the repeated 
    division will eventually yield 1 and that the divisor is non-zero.
        
    Args:
        a (int): The integer to be reduced to one.
        b (int): The divisor used for each integer division.
    
    Returns:
        int: The total number of division operations performed.
    """
    count = 0
    while a != 1:
        a //= b
        count += 1
    return count


# Example usage:
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
operations = divide_until_one(a, b)
print("Number of division operations:", operations)

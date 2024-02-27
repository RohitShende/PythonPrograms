"""
Program to divide a number `a` by `b` until it becomes 1 and count the number of
division operations it takes
"""


def divide_until_one(a, b):
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

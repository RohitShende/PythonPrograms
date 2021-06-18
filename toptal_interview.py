# A vending machine has the following denominations: 1c, 5c, 10c, 25c, 50c, and $1.
# Your task is to write a program that will be used in a vending machine to return change.
# Assume that the vending machine will always want to return the least number of coins or notes.
# Devise a function getChange(M, P) where M is how much money was inserted
# into the machine and P the price of the item selected,
# that returns an array of integers representing the number of each denomination to return.
#
# Example:
# getChange(5, 0.99) // should return [1,0,0,0,0,4]
import math


def getChange(M, P):
    change = [1, 5, 10, 25, 50, 100]  # in c
    change_left = int(M*100 - P*100)
    # print(change_left)
    result = [0, 0, 0, 0, 0, 0]
    # print(change_left)
    for i in range(len(change) - 1, -1, -1):
        # print(i, change[i])
        result[i] = change_left // change[i]
        change_left = change_left % change[i]
        # print(result[i])
        # print(change_left)
    return result


result = getChange(5, 0.99)
print(result)
assert result == [1, 0, 0, 0, 0, 4]
result = getChange(3.14, 1.99)
print(result)
assert result == [0, 1, 1, 0, 0, 1]
result = getChange(4, 3.14)
print(result)
assert result == [1, 0, 1, 1, 1, 0]
result = getChange(0.45, 0.34)
print(result)
assert result == [1, 0, 1, 0, 0, 0]

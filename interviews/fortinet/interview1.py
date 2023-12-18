"""
Find the unique second-largest element from the array of numbers
arr = [-1,3,2,-5,6,8,7,3,8,0]
output : 7

Assumptions:
1. Not sorted
2. negative numbers
3. duplicates
4. size > 2

"""

arr = [-1, 3, 2, -5, 6, 8, 7, 3, 8, 0]


# arr.sort(reverse=True) O(nlogn)

# two pointers - highest, second_highest O(n)

def second_highest(arr: list):
    if not arr:
        return None

    if len(arr) < 2:
        return None

    curr_h = float("-inf")
    sec_h = float("-inf")

    for num in arr:
        if num > curr_h:
            sec_h = curr_h
            curr_h = num
        elif num > sec_h and num != curr_h:
            sec_h = num

    return sec_h


assert second_highest([-1, 3, 2, -5, 6, 8, 7, 3, 8, 0]) == 7
assert second_highest([1, 2, 3, 4, 5]) == 4
assert second_highest([5, 4, 3, 2, 1]) == 4
assert second_highest([8, 8, 8, 8, 8]) == float("-inf")
assert second_highest([-5, -3, -1, -6]) == -3
assert second_highest([8, 8, 7, 7, 6, 8, 9]) == 8
assert second_highest([]) is None
assert second_highest(None) is None

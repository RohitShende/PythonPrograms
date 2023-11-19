# give all subsets
arr = [1, 2, 3, 4] # , 5, 6, 7, 8, 9, 10]
output = [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]


def subString(s, n):
    # Pick starting point in outer loop
    # and lengths of different strings for
    # a given starting point
    result = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            result.append(s[start:end])
    return result


def sub(arr):
    if not arr:
        return tuple()
    else:
        result = set()
        for i in range(len(arr)):  # n
            result.add((arr[i],))   # n
            for j in sub(arr[i+1:]):
                result.add((arr[i],) + j)
        return result

"""
10 -> 10......1
         8  6
        9  7  5
         8   6  4
          7   5  3

fib => 2 ^ n -> operation -> 2 -> 2 -> 2
10*9*8*7*6..1 + 9*8*7...1 + 8*7*6...1 .... + 1 == 2^n
"""

sub_arrays = sub(arr)
print(len(sub_arrays))
print(sub_arrays)


sub_arrays = subString(arr, 4)
print(len(sub_arrays))
print(sub_arrays)

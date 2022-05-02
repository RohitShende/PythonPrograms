"""
// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
// You may assume that the intervals were initially sorted according to their start times.
// Given intervals [1, 3], [6, 9] insert and merge [2, 5]: [ [1, 5], [6, 9] ]
// Given intervals [1, 3], [6, 9] insert and merge [2, 6]: [ [1, 9] ]

****************************************************************************
This solution can also be used for another problem called merge intervals,
where the intervals are given which are not sorted.
Input: intervals = [[1,3],[2,6],[15,18],[8,10]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Only change we need to do is to sort the list of intervals based on start of the interval
"""


def get_place(arr: list[tuple], x: int):
    pos = 0
    for i, (s, e) in enumerate(arr):
        if x > s:
            pos = i+1
    return pos


def merge(arr: list[tuple[int, int]]) -> list[tuple[int, int]]:
    result = []
    for interval in arr:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


def place_interval_in_list(arr: list[tuple], interval: tuple[int, int]) -> list[tuple]:
    x, y = interval
    # find the places of x and y
    x_place = get_place(arr, x)
    print(arr, interval)
    arr.insert(x_place, interval)
    return merge(arr)


if __name__ == '__main__':
    testcases = [
        [{"arr": [[1, 3], [6, 9]], "interval": [1, 5]}, [[1, 5], [6, 9]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [2, 5]}, [[1, 5], [6, 9]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [2, 6]}, [[1, 9]]],
        [{"arr": [[2, 3], [6, 9]], "interval": [1, 9]}, [[1, 9]]],
        [{"arr": [[2, 3], [6, 9]], "interval": [1, 7]}, [[1, 9]]],
        [{"arr": [[2, 3], [6, 9]], "interval": [1, 11]}, [[1, 11]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [10, 12]}, [[1, 3], [6, 9], [10, 12]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [2, 12]}, [[1, 12]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [3, 13]}, [[1, 13]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [7, 13]}, [[1, 3], [6, 13]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [5, 12]}, [[1, 3], [5, 12]]],
        [{"arr": [[1, 3], [6, 9]], "interval": [5, 8]}, [[1, 3], [5, 9]]],
        [{"arr": [[1, 3], [6, 9], [11, 14]], "interval": [5, 10]}, [[1, 3], [5, 10], [11, 14]]],
        [{"arr": [], "interval": [5, 10]}, [[5, 10]]],
    ]
    for inputs, expected_output in testcases:
        actual_output = place_interval_in_list(**inputs)
        print(actual_output, "\n")
        assert actual_output == expected_output

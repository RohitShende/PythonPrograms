"""
// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
// You may assume that the intervals were initially sorted according to their start times.
// Given intervals [1, 3], [6, 9] insert and merge [2, 5]: [ [1, 5], [6, 9] ]
// Given intervals [1, 3], [6, 9] insert and merge [2, 6]: [ [1, 9] ]
"""


def get_place(arr: list[tuple], x: int, for_start=False):
    for i, (s, e) in enumerate(arr):
        if x < s:
            if for_start:
                if i > 0 and arr[i-1][1] < x:
                    return i
                else:
                    return i-1
            else:
                return i-1

        if x <= e:
            return i

    if x > arr[-1][1]:
        return len(arr)

    return -1


def place_interval_in_list(arr: list[tuple], interval: tuple[int, int]) -> list[tuple]:
    x, y = interval
    n = len(arr)
    # find the places of x and y
    x_place = get_place(arr, x, for_start=True)
    y_place = get_place(arr, y)
    print(arr, interval)
    # print(f"x : {x_place}, \t y: {y_place}")

    # interval does not have overlap with list
    if y_place == -1:
        return [interval] + arr

    if x_place == n:
        return arr + [interval]

    # interval is bigger than list
    if x_place == -1 and y_place == n:
        return [interval]

    # interval is inside the list
    if x_place > -1 and y_place < n:
        return arr[:x_place] + [(min(x, arr[x_place][0]), max(y, arr[y_place][1]))] + arr[y_place+1:]

    # interval is half inside and half outside the list
    elif x_place == -1 and y_place < n:
        return [(x, max(y, arr[y_place][1]))] + arr[y_place+1:]
    else:
        return arr[:x_place] + [(min(x, arr[x_place][0]), y)]


if __name__ == '__main__':
    testcases = [
        [{"arr": [(1, 3), (6, 9)], "interval": (2, 5)}, [(1, 5), (6, 9)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (2, 6)}, [(1, 9)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (-1, 9)}, [(-1, 9)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (-1, 7)}, [(-1, 9)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (-1, 11)}, [(-1, 11)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (10, 12)}, [(1, 3), (6, 9), (10, 12)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (2, 12)}, [(1, 12)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (3, 13)}, [(1, 13)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (7, 13)}, [(1, 3), (6, 13)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (5, 12)}, [(1, 3), (5, 12)]],
        [{"arr": [(1, 3), (6, 9)], "interval": (5, 8)}, [(1, 3), (5, 9)]],
        [{"arr": [(1, 3), (6, 9), (11, 14)], "interval": (5, 10)}, [(1, 3), (5, 10), (11, 14)]],

    ]
    for inputs, expected_output in testcases:
        actual_output = place_interval_in_list(**inputs)
        print(actual_output, "\n")
        assert actual_output == expected_output

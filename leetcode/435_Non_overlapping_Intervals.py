from typing import List


# Problem: https://leetcode.com/problems/non-overlapping-intervals/


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals_removed = 0
    intervals.sort(key=lambda x: x[1])

    print(intervals)
    last = 0
    curr = 1
    while curr < len(intervals):
        print(last, curr)
        print(intervals[last], intervals[curr])
        if intervals[curr][0] < intervals[last][1]:
            if intervals[curr][1] < intervals[last][1]:
                # full curr inside last
                print("full curr inside last")
                last += 1
                intervals_removed += 1
                intervals.pop(curr)
            else:
                # part overlap
                print("part overlap")
                intervals_removed += 1
                intervals.pop(curr)
        else:
            last += 1
            curr += 1

    return intervals_removed


if __name__ == '__main__':
    ip_intervals = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
    expected_result = 2
    result = eraseOverlapIntervals(ip_intervals)
    assert expected_result == result

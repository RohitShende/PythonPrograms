"""
Check if the given intervals overlap with each other
if they overlap return True else return False

sample 1:
i1 = (1, 2)
i2 = (3, 5)

o/p - False

sample 2:
i1 = (1, 6)
i2 = (3, 5)

o/p - True

"""


# def is_interval_overlapping(i1: tuple, i2: tuple) -> bool:
#     x1, y1 = i1
#     x2, y2 = i2
#
#     if (x2 <= x1 <= y2) or (x1 <= x2 <= y1):
#         # overlap
#         return True
#     return False


def is_interval_overlapping(i1: tuple, i2: tuple) -> bool:
    x1, y1 = i1
    x2, y2 = i2
    return max(x1, x2) <= min(y1, y2)


if __name__ == '__main__':
    assert is_interval_overlapping((1, 6), (3, 5)) is True
    assert is_interval_overlapping((20, 40), (100, 103)) is False
    assert is_interval_overlapping((1, 10), (-5, 1)) is True
    assert is_interval_overlapping((1, 5), (5, 10)) is True
    assert is_interval_overlapping((1, 6), (7, 10)) is False
    assert is_interval_overlapping((1, 20), (5, 7)) is True
    assert is_interval_overlapping((4, 13), (2, 20)) is True


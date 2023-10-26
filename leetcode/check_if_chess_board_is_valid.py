"""
Check if the chess board is valid
Given co-ordinates of 2 Queens and
a size "N" for the square chess board

The chess board will be of N x N size square.
Check if they kill each other.
Queen moves -> horizontal, vertical and diagonal

return True if queens do not kill each other. Means the board is valid
else return False

Constraints:
q1 != q2
2 <= n <= 9

Sample input 1:
n = 4
q1 = (0,0)
q2 = (2,2)

output:
False

explanation:

The chess board looks like below:

Q - - -
- - - -
- - Q -
- - - -

The Queen 2 comes in the diagonal of Queen 1 hence the board is NOT Valid


Sample input 2:
n = 4
q1 = (0,0)
q2 = (2,3)

output:
True

explanation:

The chess board looks like below:

Q - - -
- - - -
- - - Q
- - - -

The Queen 1 and Queen 2 do not kill each other
Hence board is Valid

"""


def is_board_valid(n: int, q1: tuple, q2: tuple) -> bool:
    x1, y1 = q1
    x2, y2 = q2

    # horizontal
    if x1 == x2:
        return False

    # vertical
    if y1 == y2:
        return False

    # diagonal
    if abs(x1 - x2) == abs(y1 - y2):
        return False

    return True


if __name__ == '__main__':
    assert is_board_valid(5, (1, 1), (2, 3)) is True  # valid
    assert is_board_valid(8, (4, 3), (6, 7)) is True  # valid
    assert is_board_valid(8, (1, 2), (3, 5)) is True  # valid

    assert is_board_valid(4, (0, 0), (0, 2)) is False  # horizontal
    assert is_board_valid(4, (3, 2), (1, 2)) is False  # vertical
    assert is_board_valid(4, (0, 0), (2, 2)) is False  # diagonal
    assert is_board_valid(8, (2, 1), (4, 3)) is False  # diagonal

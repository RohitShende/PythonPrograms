import time
from copy import deepcopy
from typing import List


class Chess:
    def __init__(self, number_of_squares, sleep_after_operation=0):
        self.N = number_of_squares
        self.sleep = sleep_after_operation
        self.board = [
            ['.' for _ in range(self.N)]
            for _ in range(self.N)
        ]
        print(f'Board initialized for N = {self.N}')
        self.print_board()
        self.all_possibilities = []

    def print_all_possibilities(self):
        print("All Possibilities : \n")
        temp = deepcopy(self.board)
        for i, board in enumerate(self.all_possibilities):
            self.board = board
            print(f"Possibility No: {i + 1}")
            self.print_board()
        self.board = temp

    def print_board(self):
        print('\n----------- Board -----------')
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()
        print('-------------------------------\n')

    def is_valid_coordinate(self, r, c):
        if 0 <= r < self.N and 0 <= c < self.N:
            return True
        return False

    def does_queen_kill(self, r, c) -> bool:
        # check same row
        for j in range(self.N):
            if j != c and self.board[r][j] == 'Q':
                return True

        # check same col
        for i in range(self.N):
            if i != r and self.board[i][c] == 'Q':
                return True

        # check diagonals
        fd = [(i, i + (c - r)) for i in range(self.N) if self.is_valid_coordinate(i, i + (c - r))]
        bd = [(i, (self.N - i) + (c + r - self.N)) for i in range(self.N) if
              self.is_valid_coordinate(i, (self.N - i) + (c + r - self.N))]
        for coord in fd + bd:
            i, j = coord
            if i != r and j != c and self.board[i][j] == 'Q':
                return True

        return False

    def is_board_valid(self) -> bool:
        for row in range(self.N):
            for col in range(self.N):
                if self.board[row][col] == 'Q':
                    if self.does_queen_kill(row, col):
                        return False
        return True

    def mark_queen_at_pos(self, r, c) -> bool:
        self.board[r][c] = 'Q'
        if not self.is_board_valid():
            print('Wrong position of Queen')
            self.print_board()
            if self.sleep:
                time.sleep(self.sleep)
            self.board[r][c] = '.'
            return False
        print(f"Queen correctly placed in column {c+1}...")
        self.print_board()
        if self.sleep:
            time.sleep(self.sleep)
        return True

    def un_mark_queen_at_pos(self, r, c):
        self.board[r][c] = '.'

    def backtrack(self, col=0):
        if col == self.N:
            # board has been marked with N queens
            # we can store the result now
            solution = [''.join(i) for i in self.board]
            self.all_possibilities.append(solution)
            print("Possibility Captured")
            self.print_board()
            print("\n\n\n")
            if self.sleep:
                time.sleep(self.sleep*3)
            return

        for row in range(self.N):
            if self.mark_queen_at_pos(row, col):
                # mark queen in next col
                self.backtrack(col=col + 1)
                self.un_mark_queen_at_pos(row, col)

    def place_queen(self) -> List:
        self.backtrack()
        self.print_all_possibilities()
        return self.all_possibilities


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess = Chess(number_of_squares=n)
        return chess.place_queen()


if __name__ == '__main__':
    n = 1
    result = Solution().solveNQueens(n)
    expected_result = [['Q']]
    assert sorted(result) == sorted(expected_result)

    n = 4
    result = Solution().solveNQueens(n)
    expected_result = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    assert sorted(result) == sorted(expected_result)

    n = 9
    result = Solution().solveNQueens(n)

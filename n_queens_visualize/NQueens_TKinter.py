import tkinter as tk
import time
from tkinter import Button, Label, Entry, Toplevel
from functools import partial
from threading import Thread
from n_queens_visualize.n_queens_backend import Chess

root = tk.Tk()


class ChessBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=64, color1="#a7ab90", color2="#0e140c"):
        '''size is the size of a square, in pixels'''
        self.parent = parent
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.queen = tk.PhotoImage(file="chess_queen.png")
        canvas_width = columns * size
        canvas_height = rows * size
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="khaki")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.center_window(width=canvas_width, height=canvas_height)
        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def center_window(self, width=300, height=200):
        # get screen width and height
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size / 2)
        y0 = (row * self.size) + int(self.size / 2)
        self.canvas.coords(name, x0, y0)

    def clear_pieces(self):
        """ Clear all the existing pieces """
        self.pieces = {}
        self.canvas.delete("piece")

    def refresh(self, event=None):
        '''Redraw the board, possibly in response to window being resized'''
        if event:
            xsize = int((event.width - 1) / self.columns)
            ysize = int((event.height - 1) / self.rows)
            self.size = min(xsize, ysize)

        self.canvas.delete("square")
        for row in range(self.rows):
            if row % 2 == 0:
                color = self.color1
            else:
                color = self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def convert_board_to_positions(self, curr_board):
        curr_board = [list(i) for i in curr_board]
        positions = []
        for i in range(self.rows):
            for j in range(self.columns):
                if curr_board[i][j] == 'Q':
                    positions.append((i, j))
        return positions

    def highlight_solution(self, positions):
        self.canvas.update()

    def fetch_curr_board(self, chess, window):
        print("**************************   fetch_curr_board_called")
        curr_board = chess.board
        curr_positions = self.convert_board_to_positions(curr_board)
        print("Curr Positions : ", curr_positions)

        self.clear_pieces()
        print("Pieces cleared")

        for index, position in enumerate(curr_positions):
            i, j = position
            print('Adding piece', f"queen-{index} at", i, j)
            self.addpiece(f"queen-{index}", self.queen, i, j)
        # self.highlight_solution(curr_positions)
        self.refresh()

        window.after(500, self.fetch_curr_board, chess, window)


def start_processing(n_entry):
    n = int(n_entry.get())

    # hide old window
    root.withdraw()

    chess_window = Toplevel()
    chess_window.title(f"{n} Queen's Problem")
    board = ChessBoard(chess_window, rows=n, columns=n)
    board.pack(side="top", fill="both", expand="true", padx=10, pady=10)

    chess = Chess(number_of_squares=n, sleep_after_operation=2)

    thread = Thread(name='chess_backend', target=chess.place_queen)
    thread.start()

    chess_window.after(1, board.fetch_curr_board, chess, chess_window)
    chess_window.mainloop()


def main():
    root.title("N Queen's Problem")

    # centering the root window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (400 / 2)
    y = (screen_height / 2) - (100 / 2)
    root.geometry('%dx%d+%d+%d' % (400, 100, x, y))

    # Label
    label = Label(root, text="Enter N (1-9):")

    # Entry for user input
    entry = Entry(root, validate='focus', )

    # Define callable function with printDetails function and usernameEntry argument
    start_processing_callable = partial(start_processing, entry)

    # Submit button
    submit_button = Button(root, text="Submit", command=start_processing_callable)

    # Place label, entry, and button in grid
    label.grid(row=0, column=0)
    entry.grid(row=0, column=1)
    submit_button.grid(row=1, column=1)

    root.mainloop()


if __name__ == "__main__":
    main()


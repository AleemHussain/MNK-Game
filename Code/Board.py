import numpy as np

class Board:
    """
    Represents the game board. It holds the grid and provides methods to display
    and check for winning conditions.
    """

    def __init__(self, rows, cols, k):
        self.rows = rows  # Number of rows
        self.cols = cols  # Number of columns
        self.k = k  # Winning condition (k in a row)
        self.grid = np.zeros((rows, cols), dtype=int)  # Initialize board with zeros

    def display(self):
        """Displays the board in a readable format."""
        print("\nCurrent Board:")
        for row in self.grid:
            print(" ".join(str(int(cell)) for cell in row))
        print()

    def is_valid_move(self, row, col):
        """Checks if a move is within bounds and the cell is empty."""
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row, col] == 0

    def make_move(self, row, col, player_number):
        """Places a move on the board if valid."""
        if self.is_valid_move(row, col):
            self.grid[row, col] = player_number
            return True
        return False

    def has_won(self, player_number):
        """
        Checks if the given player has won anywhere on the board.
        """

        def check_line(line):
            """Helper function to check if a line contains k consecutive player marks."""
            count = 0
            for element in line:
                if element == player_number:
                    count += 1
                    if count == self.k:
                        return True
                else:
                    count = 0
            return False

        # Check rows and columns
        for row in range(self.rows):
            if check_line(self.grid[row, :]):  # Check row
                return True

        for col in range(self.cols):
            if check_line(self.grid[:, col]):  # Check column
                return True

        # Check diagonals
        for d in range(-self.rows + 1, self.cols):
            if check_line(self.grid.diagonal(d)) or check_line(np.fliplr(self.grid).diagonal(d)):
                return True

        return False

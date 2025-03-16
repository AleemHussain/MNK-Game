import numpy as np

class Board:
    """
    Represents the game board. It holds the grid and provides methods to display 
    and check for winning conditions.
    """

    def __init__(self, m, n, k):
        self.m = m  # Number of rows
        self.n = n  # Number of columns
        self.k = k  # Winning condition (k in a row)
        self.array = np.zeros((m, n), dtype=int)  # Initialize board with zeros

    def display(self):
        """
        Displays the board in a more readable format.
        """
        print("\nCurrent Board:")
        for row in self.array:
            print(" ".join(str(int(cell)) for cell in row))
        print()

    def has_won(self, row, col, player_number):
        """
        Checks if the given player has won after placing a move at (row, col).
        Winning conditions: k consecutive pieces in a row, column, or diagonal.
        """

        def check_line(line):
            """
            Helper function to check if a line contains k consecutive player marks.
            """
            count = 0
            for element in line:
                if element == player_number:
                    count += 1
                    if count == self.k:
                        return True
                else:
                    count = 0
            return False

        # Check row
        if check_line(self.array[row, :]):
            return True

        # Check column
        if check_line(self.array[:, col]):
            return True

        # Check main and anti-diagonal (↘ and ↙)
        for d in range(-self.m + 1, self.n):
            if check_line(self.array.diagonal(d)) or check_line(np.fliplr(self.array).diagonal(d)):
                return True

        return False

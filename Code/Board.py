import numpy as np

class Board:
    """
    Represents the game board for an MNK game.
    It holds the grid and provides methods for displaying the board,
    making moves, and checking for winning conditions.
    """

    def __init__(self, rows, cols, k):
        """
        Initializes the game board.

        :param rows: Number of rows in the board.
        :param cols: Number of columns in the board.
        :param k: Number of consecutive marks needed to win.
        """
        self.rows = rows  # Number of rows
        self.cols = cols  # Number of columns
        self.k = k  # Winning condition (k in a row)
        self.grid = np.zeros((rows, cols), dtype=int)  # Create an empty board with zeros

    def display(self):
        """
        Displays the current state of the board in a readable format.
        Converts numerical values to strings for better visualization.
        """
        print("\nCurrent Board:")
        for row in self.grid:
            print(" ".join(str(int(cell)) for cell in row))  # Convert each cell to integer and print
        print()

    def is_valid_move(self, row, col):
        """
        Checks whether a move is valid.
        A move is valid if:
        - It is within the bounds of the board.
        - The chosen cell is currently empty.

        :param row: Row index of the move.
        :param col: Column index of the move.
        :return: True if the move is valid, False otherwise.
        """
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row, col] == 0

    def make_move(self, row, col, player_number):
        """
        Places a move on the board if the move is valid.

        :param row: Row index where the move is placed.
        :param col: Column index where the move is placed.
        :param player_number: Player's number (1 or 2) to place on the board.
        :return: True if the move was successful, False otherwise.
        """
        if self.is_valid_move(row, col):
            self.grid[row, col] = player_number  # Place the player's mark on the board
            return True
        return False  # Move is invalid

    def has_won(self, player_number):
        """
        Checks whether the specified player has won the game.

        A player wins if they have 'k' consecutive marks in:
        - A row
        - A column
        - A diagonal (main or anti-diagonal)

        :param player_number: The player's number to check for a win.
        :return: True if the player has won, False otherwise.
        """

        def check_line(line):
            """
            Helper function to check if a given sequence (row, column, or diagonal)
            contains 'k' consecutive occurrences of the player's mark.

            :param line: A sequence (row, column, or diagonal) to check.
            :return: True if the sequence contains 'k' consecutive marks, False otherwise.
            """
            count = 0  # Counter for consecutive player marks
            for element in line:
                if element == player_number:
                    count += 1  # Increment count if the mark matches the player's number
                    if count == self.k:  # If k consecutive marks are found, return True
                        return True
                else:
                    count = 0  # Reset count if sequence is broken
            return False

        # Check rows for a win
        for row in range(self.rows):
            if check_line(self.grid[row, :]):  # Check each row
                return True

        # Check columns for a win
        for col in range(self.cols):
            if check_line(self.grid[:, col]):  # Check each column
                return True

        # Check diagonals for a win
        for d in range(-self.rows + 1, self.cols):  # Covers all possible diagonals
            if check_line(self.grid.diagonal(d)):  # Main diagonal check
                return True
            if check_line(np.fliplr(self.grid).diagonal(d)):  # Anti-diagonal check
                return True

        return False  # No win detected

import sys
import os
import unittest
import numpy as np

# Add the parent directory to sys.path to allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Board import Board  # Import the Board class for testing


class TestBoard(unittest.TestCase):
    """
    Unit tests for the Board class.
    """

    def setUp(self):
        """
        Set up a default 3x3 game board with a win condition of 3 in a row.
        This method runs before each test.
        """
        self.board = Board(3, 3, 3)  # 3x3 board with 3-in-a-row to win

    def test_initialization(self):
        """
        Test if the board initializes correctly with the correct shape.
        """
        self.assertEqual(self.board.grid.shape, (3, 3))  # Ensure grid is 3x3
        self.assertTrue(np.all(self.board.grid == 0))  # Check if all cells are empty (0)

    def test_make_move(self):
        """
        Test the make_move function:
        - A move should be placed successfully if the cell is empty.
        - A move should fail if the cell is already occupied.
        """
        self.assertTrue(self.board.make_move(0, 0, 1))  # Player 1 places move at (0,0)
        self.assertFalse(self.board.make_move(0, 0, 2))  # Player 2 attempts to place move at (0,0) again

    def test_has_won(self):
        """
        Test the winning condition detection:
        - A diagonal win should be recognized when player 1 places three marks in a diagonal.
        """
        self.board.make_move(0, 0, 1)
        self.board.make_move(1, 1, 1)
        self.board.make_move(2, 2, 1)
        self.assertTrue(self.board.has_won(1))  # Player 1 should have won

    def test_invalid_move(self):
        """
        Test that an invalid move (out of bounds) is correctly rejected.
        """
        self.assertFalse(self.board.make_move(-1, 0, 1))  # Negative row index
        self.assertFalse(self.board.make_move(3, 3, 1))  # Index outside the board

    def test_draw_condition(self):
        """
        Test a draw scenario where no player wins and the board is full.
        """
        moves = [
            (0, 0, 1), (0, 1, 2), (0, 2, 1),
            (1, 0, 2), (1, 1, 1), (1, 2, 2),
            (2, 0, 2), (2, 1, 1), (2, 2, 2),
        ]
        for row, col, player in moves:
            self.board.make_move(row, col, player)

        self.assertFalse(self.board.has_won(1))  # No win for Player 1
        self.assertFalse(self.board.has_won(2))  # No win for Player 2
        self.assertFalse(np.any(self.board.grid == 0))  # No empty cells (board is full)

if __name__ == '__main__':
    unittest.main()

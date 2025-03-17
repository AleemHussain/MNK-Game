import sys
import os
import unittest
import numpy as np

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3, 3)  # Example setup for a 3x3 board with 3-in-a-row win condition

    def test_initialization(self):
        self.assertEqual(self.board.grid.shape, (3, 3))  # Assuming `grid` is a NumPy array

    def test_make_move(self):
        self.assertTrue(self.board.make_move(0, 0, 1))  # Assuming move (0,0) with player 1 is valid
        self.assertFalse(self.board.make_move(0, 0, 2))  # Should not allow move in the same spot

    def test_has_won(self):
        self.board.make_move(0, 0, 1)
        self.board.make_move(1, 1, 1)
        self.board.make_move(2, 2, 1)
        self.assertTrue(self.board.has_won(1))  # Check if player 1 won

if __name__ == '__main__':
    unittest.main()

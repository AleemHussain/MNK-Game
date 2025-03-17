import unittest
import numpy as np
from Board import Board  # Assuming the Board class is implemented in Board.py

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        """Initialize a fresh board before each test."""
        self.rows = 3
        self.cols = 3
        self.k = 3
        self.board = Board(self.rows, self.cols, self.k)
    
    def test_board_initialization(self):
        """Test if the board initializes correctly."""
        self.assertEqual(self.board.rows, self.rows)
        self.assertEqual(self.board.cols, self.cols)
        self.assertEqual(self.board.k, self.k)
        self.assertTrue(np.array_equal(self.board.grid, np.zeros((self.rows, self.cols), dtype=int)))
    
    def test_valid_move(self):
        """Test if a move is valid and properly placed."""
        self.assertTrue(self.board.is_valid_move(1, 1))
        self.board.make_move(1, 1, 1)
        self.assertEqual(self.board.grid[1, 1], 1)
    
    def test_invalid_move(self):
        """Test if an invalid move is rejected."""
        self.board.make_move(1, 1, 1)
        self.assertFalse(self.board.is_valid_move(1, 1))  # Spot already taken
    
    def test_out_of_bounds_move(self):
        """Test if out-of-bounds moves are rejected."""
        self.assertFalse(self.board.is_valid_move(-1, 0))
        self.assertFalse(self.board.is_valid_move(self.rows, self.cols))
    
    def test_win_condition_horizontal(self):
        """Test if the game correctly detects a horizontal win."""
        for col in range(self.k):
            self.board.make_move(1, col, 1)
        self.assertTrue(self.board.has_won(1))
    
    def test_win_condition_vertical(self):
        """Test if the game correctly detects a vertical win."""
        for row in range(self.k):
            self.board.make_move(row, 1, 1)
        self.assertTrue(self.board.has_won(1))
    
    def test_win_condition_diagonal(self):
        """Test if the game correctly detects a diagonal win."""
        for i in range(self.k):
            self.board.make_move(i, i, 1)
        self.assertTrue(self.board.has_won(1))
    
    def test_no_win(self):
        """Test if the game correctly identifies no win when board is incomplete."""
        self.board.make_move(0, 0, 1)
        self.board.make_move(0, 1, 2)
        self.board.make_move(1, 1, 1)
        self.assertFalse(self.board.has_won(1))
        self.assertFalse(self.board.has_won(2))
    
    def test_full_board_no_win(self):
        """Test if the game correctly handles a draw scenario."""
        moves = [
            (0, 0, 1), (0, 1, 2), (0, 2, 1),
            (1, 0, 2), (1, 1, 1), (1, 2, 2),
            (2, 0, 1), (2, 1, 1), (2, 2, 2)
        ]
        for row, col, player in moves:
            self.board.make_move(row, col, player)
        self.assertFalse(self.board.has_won(1))
        self.assertFalse(self.board.has_won(2))

if __name__ == '__main__':
    unittest.main()
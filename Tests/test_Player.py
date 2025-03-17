import sys
import os
import unittest
import numpy as np
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Board import Board
from Code.Player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        """Initialize board and player before each test."""
        self.rows = 3
        self.cols = 3
        self.k = 3
        self.board = Board(self.rows, self.cols, self.k)
        self.player = Player("Test Player", 1, 0)
    
    def test_player_initialization(self):
        """Test if the player initializes correctly."""
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.number, 1)
        self.assertEqual(self.player.mode, 0)
    
    def test_valid_move(self):
        """Test if a valid move is accepted."""
        self.board.grid[1, 1] = 0  # Ensure the position is free
        with mock.patch('builtins.input', side_effect=["2", "2"]):
            row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual((row, col), (1, 1))
    
    def test_invalid_move_out_of_bounds(self):
        """Test if an out-of-bounds move is rejected."""
        with mock.patch('builtins.input', side_effect=["4", "4", "2", "2"]):
            row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual((row, col), (1, 1))  # Should retry and pick a valid move
    
    def test_invalid_move_occupied(self):
        """Test if an occupied position is rejected."""
        self.board.grid[1, 1] = 2  # Position occupied by another player
        with mock.patch('builtins.input', side_effect=["2", "2", "1", "1"]):
            row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual((row, col), (0, 0))  # Should retry and pick a valid move
    
    def test_invalid_input_handling(self):
        """Test if non-numeric input is handled gracefully."""
        with mock.patch('builtins.input', side_effect=["a", "b", "2", "2"]):
            row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual((row, col), (1, 1))  # Should retry and pick a valid move
    
if __name__ == "__main__":
    unittest.main()

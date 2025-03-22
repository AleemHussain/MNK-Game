import sys
import os
import unittest
import numpy as np
from unittest import mock

# Add the parent directory to sys.path to allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Board import Board  # Import Board class
from Code.Player import Player  # Import Player class


class TestPlayer(unittest.TestCase):
    """
    Unit tests for the Player class.
    """

    def setUp(self):
        """
        Initialize the board and a test player before each test.
        """
        self.rows = 3
        self.cols = 3
        self.k = 3  # Win condition: 3 in a row
        self.board = Board(self.rows, self.cols, self.k)  # Create a new game board
        self.player = Player("Test Player", 1, 0)  # Create a human player (mode 0)

    def test_player_initialization(self):
        """
        Test if the player initializes correctly with the expected attributes.
        """
        self.assertEqual(self.player.name, "Test Player")  # Verify player name
        self.assertEqual(self.player.number, 1)  # Verify player number
        self.assertEqual(
            self.player.mode, 0
        )  # Verify player mode (irrelevant for humans)

    @mock.patch("builtins.input", side_effect=["2", "2"])
    def test_valid_move(self, mock_input):
        """
        Test if a valid move is accepted and returned correctly.
        """
        self.board.grid[1, 1] = 0  # Ensure the position is free
        row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual(
            (row, col), (1, 1)
        )  # Check if the move is correctly registered

    @mock.patch("builtins.input", side_effect=["4", "4", "2", "2"])
    def test_invalid_move_out_of_bounds(self, mock_input):
        """
        Test if an out-of-bounds move is rejected and a valid move is eventually accepted.
        """
        row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual(
            (row, col), (1, 1)
        )  # Should retry and pick a valid move inside the board

    @mock.patch("builtins.input", side_effect=["2", "2", "1", "1"])
    def test_invalid_move_occupied(self, mock_input):
        """
        Test if an occupied position is rejected and a valid move is eventually accepted.
        """
        self.board.grid[1, 1] = 2  # Position already occupied by another player
        row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual((row, col), (0, 0))  # Should retry and pick a valid move

    @mock.patch("builtins.input", side_effect=["a", "b", "2", "2"])
    def test_invalid_input_handling(self, mock_input):
        """
        Test if non-numeric input is handled gracefully and a valid move is eventually accepted.
        """
        row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual((row, col), (1, 1))  # Should retry and pick a valid move

    @mock.patch("builtins.input", side_effect=["1", "1", "2", "2"])
    def test_valid_move_first_try(self, mock_input):
        """
        Test if a valid move is accepted on the first try without retries.
        """
        row, col = self.player.make_move(self.player.number, self.board)
        self.assertEqual((row, col), (0, 0))  # Should take the first valid input


if __name__ == "__main__":
    unittest.main()

import sys
import os
import unittest
from unittest.mock import patch

# Add the parent directory to sys.path to allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Game import Game  # Import the Game class
from Code.Board import Board  # Import the Board class
from Code.Player import Player  # Import the Player class
from Code.MyBot import MyBot  # Import the MyBot class (AI Player)


class TestGame(unittest.TestCase):
    """
    Unit tests for the Game class.
    """

    def setUp(self):
        """
        Set up a simple 3x3 game before each test.
        """
        self.rows = 3
        self.cols = 3
        self.k = 3  # Win condition: 3 in a row
        self.player1 = Player("Alice", 1, 0)  # Human player 1
        self.player2 = Player("Bob", 2, 0)  # Human player 2
        self.game = Game(self.rows, self.cols, self.k, self.player1, self.player2)  # Create a new game instance

    def test_game_initialization(self):
        """
        Test if the game initializes properly with correct attributes.
        """
        self.assertEqual(self.game.board.rows, self.rows)  # Check rows
        self.assertEqual(self.game.board.cols, self.cols)  # Check columns
        self.assertEqual(self.game.player1.name, "Alice")  # Check player 1 name
        self.assertEqual(self.game.player2.name, "Bob")  # Check player 2 name

    def test_board_initialization(self):
        """
        Test if the board is initialized correctly with the correct shape.
        """
        self.assertEqual(self.game.board.grid.shape, (self.rows, self.cols))  # Check board dimensions
        self.assertTrue((self.game.board.grid == 0).all())  # Check if board starts empty

    def test_bot_move(self):
        """
        Test if a bot can successfully make a move.
        Ensures that the move is within bounds.
        """
        bot = MyBot("Bot", 1, 1)  # Create a bot player with mode 1 (random)
        row, col = bot.make_move(bot.number, self.game.board, bot.mode)  # Get bot's move
        self.assertTrue(0 <= row < self.rows)  # Ensure row is within bounds
        self.assertTrue(0 <= col < self.cols)  # Ensure column is within bounds
        self.assertEqual(self.game.board.grid[row, col], 0)  # Ensure the chosen cell was originally empty

    @patch("builtins.input", side_effect=["1", "1"])  # Mock user input
    def test_human_move(self, mock_input):
        """
        Test if a human player can make a move.
        Mocks user input and checks if the move is successfully placed.
        """
        row, col = self.player1.make_move(self.player1.number, self.game.board)
        self.assertEqual((row, col), (0, 0))  # Check if correct move was returned
        self.assertTrue(self.game.board.is_valid_move(row, col))  # Ensure move is valid

    def test_game_loop_draw(self):
        """
        Test if the game recognizes a draw when the board is full with no winner.
        """
        moves = [
            (0, 0, 1), (0, 1, 2), (0, 2, 1),
            (1, 0, 2), (1, 1, 1), (1, 2, 2),
            (2, 0, 2), (2, 1, 1), (2, 2, 2),
        ]
        for row, col, player in moves:
            self.game.board.make_move(row, col, player)

        self.assertFalse(self.game.board.has_won(1))  # No win for Player 1
        self.assertFalse(self.game.board.has_won(2))  # No win for Player 2
        self.assertFalse((self.game.board.grid == 0).any())  # Board is completely filled

    def test_player_win(self):
        """
        Test if a player wins when they achieve the required consecutive marks.
        """
        self.game.board.make_move(0, 0, 1)
        self.game.board.make_move(0, 1, 1)
        self.game.board.make_move(0, 2, 1)  # Player 1 wins with a row
        self.assertTrue(self.game.board.has_won(1))  # Check if Player 1 is recognized as the winner
        self.assertFalse(self.game.board.has_won(2))  # Ensure Player 2 has not won


if __name__ == "__main__":
    unittest.main()

import sys
import os
import unittest
import numpy as np

# Add the parent directory to sys.path to allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Board import Board  # Import Board class
from Code.MyBot import MyBot  # Import MyBot class (AI player)
from Code.Player import Player  # Import Player class


class TestMyBot(unittest.TestCase):
    """
    Unit tests for the MyBot class.
    """

    def setUp(self):
        """
        Initialize the board and bot before each test.
        """
        self.rows = 3
        self.cols = 3
        self.k = 3  # Win condition: 3 in a row
        self.board = Board(self.rows, self.cols, self.k)  # Create a new game board
        self.bot = MyBot("Bot", 1, 3)  # Bot using Minimax AI (mode 3)

    def test_bot_random_move(self):
        """
        Test if the bot makes a valid random move in mode 1.
        """
        move = self.bot.make_move(1, self.board, mode=1)  # Mode 1: Random moves
        self.assertIsNotNone(move)  # Ensure a move is returned
        self.assertTrue(self.board.is_valid_move(*move))  # Check if move is valid

    def test_bot_block_win(self):
        """
        Test if the bot blocks an opponent's winning move in mode 2.
        """
        # Opponent (Player 2) is about to win
        self.board.make_move(0, 0, 2)
        self.board.make_move(0, 1, 2)

        move = self.bot.make_move(1, self.board, mode=2)  # Mode 2: Block or win
        self.assertEqual(move, (0, 2))  # Bot should block opponent at (0,2)

    def test_bot_win_move(self):
        """
        Test if the bot makes a winning move in mode 2.
        """
        # Bot is about to win
        self.board.make_move(1, 0, 1)
        self.board.make_move(1, 1, 1)

        move = self.bot.make_move(1, self.board, mode=2)  # Mode 2: Block or win
        self.assertEqual(move, (1, 2))  # Bot should complete its own win at (1,2)

    def test_bot_uses_minimax(self):
        """
        Test if the bot uses Minimax AI in mode 3.
        """
        move = self.bot.make_move(1, self.board, mode=3)  # Mode 3: Minimax AI
        self.assertIsNotNone(move)  # Ensure a move is returned
        self.assertTrue(self.board.is_valid_move(*move))  # Check if move is valid

    def test_bot_no_move_available(self):
        """
        Test if the bot returns None when no moves are available.
        """
        self.board.grid = np.ones((self.rows, self.cols), dtype=int)  # Fill the board
        move = self.bot.make_move(1, self.board, mode=3)  # No moves left
        self.assertIsNone(move)  # Bot should return None

    def test_bot_respects_valid_moves(self):
        """
        Test that the bot does not place a move in an occupied space.
        """
        self.board.make_move(1, 1, 1)  # Player 1 places a move at (1,1)
        move = self.bot.make_move(1, self.board, mode=1)  # Mode 1: Random move
        self.assertNotEqual(move, (1, 1))  # Ensure bot does not move to (1,1)

    def test_bot_selects_best_move_minimax(self):
        """
        Test if the bot selects the best possible move using Minimax.
        """
        # Bot is one move away from winning
        self.board.make_move(2, 0, 1)
        self.board.make_move(2, 1, 1)

        move = self.bot.make_move(1, self.board, mode=3)  # Minimax mode
        self.assertEqual(move, (2, 2))  # Bot should select the winning move

    def test_bot_blocks_strategically(self):
        """
        Test if the bot prevents an opponent's strategic win using Minimax.
        """
        # Opponent (Player 2) is close to winning
        self.board.make_move(2, 0, 2)
        self.board.make_move(2, 1, 2)

        move = self.bot.make_move(1, self.board, mode=3)  # Minimax mode
        self.assertEqual(move, (2, 2))  # Bot should block at (2,2)

if __name__ == "__main__":
    unittest.main()

import sys
import os
import unittest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Board import Board
from Code.MyBot import MyBot
from Code.Player import Player

class TestMyBot(unittest.TestCase):
    
    def setUp(self):
        """Initialize board and bot before each test."""
        self.rows = 3
        self.cols = 3
        self.k = 3
        self.board = Board(self.rows, self.cols, self.k)
        self.bot = MyBot("Bot", 1, 3)  # Bot using Minimax AI mode 3
    
    def test_bot_random_move(self):
        """Test if the bot makes a random move in mode 1."""
        move = self.bot.make_move(1, self.board, mode=1)
        self.assertIsNotNone(move)
        self.assertTrue(self.board.is_valid_move(*move))
    
    def test_bot_block_win(self):
        """Test if the bot blocks an opponent's winning move in mode 2."""
        self.board.make_move(0, 0, 2)
        self.board.make_move(0, 1, 2)
        move = self.bot.make_move(1, self.board, mode=2)
        self.assertEqual(move, (0, 2))  # Bot should block the win
    
    def test_bot_win_move(self):
        """Test if the bot makes a winning move in mode 2."""
        self.board.make_move(1, 0, 1)
        self.board.make_move(1, 1, 1)
        move = self.bot.make_move(1, self.board, mode=2)
        self.assertEqual(move, (1, 2))  # Bot should complete the win
    
    def test_bot_uses_minimax(self):
        """Test if the bot uses Minimax AI in mode 3."""
        move = self.bot.make_move(1, self.board, mode=3)
        self.assertIsNotNone(move)
        self.assertTrue(self.board.is_valid_move(*move))
    
    def test_bot_no_move_available(self):
        """Test if the bot returns None when no moves are available."""
        self.board.grid = np.ones((self.rows, self.cols), dtype=int)  # Board is full
        move = self.bot.make_move(1, self.board, mode=3)
        self.assertIsNone(move)

if __name__ == "__main__":
    unittest.main()

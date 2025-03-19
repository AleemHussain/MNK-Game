import sys
import os
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Game import Game
from Code.Board import Board
from Code.Player import Player
from Code.MyBot import MyBot

class TestGame(unittest.TestCase):
    
    def setUp(self):
        """Initialize a simple game setup before each test"""
        self.rows = 3
        self.cols = 3
        self.k = 3
        self.player1 = Player("Alice", 1, 0)
        self.player2 = Player("Bob", 2, 0)
        self.game = Game(self.rows, self.cols, self.k, self.player1, self.player2)

    def test_game_initialization(self):
        """Test if the game initializes properly"""
        self.assertEqual(self.game.board.rows, self.rows)
        self.assertEqual(self.game.board.cols, self.cols)
        self.assertEqual(self.game.player1.name, "Alice")
        self.assertEqual(self.game.player2.name, "Bob")

    def test_board_initialization(self):
        """Test if the board is initialized correctly"""
        self.assertEqual(self.game.board.grid.shape, (self.rows, self.cols))

    def test_bot_move(self):
        """Test if a bot can make a move"""
        bot = MyBot("Bot", 1, 1)
        row, col = bot.make_move(bot.number, self.game.board, bot.mode)
        self.assertTrue(0 <= row < self.rows)
        self.assertTrue(0 <= col < self.cols)

if __name__ == "__main__":
    unittest.main()
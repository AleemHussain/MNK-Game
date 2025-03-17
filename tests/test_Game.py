import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Game import Game
from Code.Board import Board
from Code.Player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        """Set up a new game instance before each test."""
        self.rows = 3
        self.cols = 3
        self.k = 3
        self.game = Game(self.rows, self.cols, self.k)

    def test_game_initialization(self):
        """Test if the game initializes correctly."""
        self.assertIsInstance(self.game.board, Board)
        self.assertEqual(self.game.board.rows, self.rows)
        self.assertEqual(self.game.board.cols, self.cols)
        self.assertEqual(self.game.board.k, self.k)

    def test_player_assignment(self):
        """Test if players are assigned correctly."""
        self.assertIsInstance(self.game.player1, Player)
        self.assertIsInstance(self.game.player2, Player)
        self.assertNotEqual(self.game.player1.symbol, self.game.player2.symbol)

    def test_valid_move_execution(self):
        """Test if a valid move updates the board."""
        self.assertTrue(self.game.board.is_valid_move(1, 1))
        self.game.play_turn(1, 1)
        self.assertFalse(self.game.board.is_valid_move(1, 1))  # Spot should be occupied

    def test_invalid_move_execution(self):
        """Test if an invalid move is not executed."""
        self.game.play_turn(0, 0)
        self.assertFalse(
            self.game.play_turn(0, 0)
        )  # Should return False, as the spot is taken

    def test_game_winning_condition(self):
        """Test if the game detects a win condition properly."""
        self.game.play_turn(0, 0)  # Player 1
        self.game.play_turn(1, 0)  # Player 2
        self.game.play_turn(0, 1)  # Player 1
        self.game.play_turn(1, 1)  # Player 2
        self.game.play_turn(0, 2)  # Player 1 wins
        self.assertTrue(self.game.board.has_won(self.game.player1.symbol))

    def test_draw_condition(self):
        """Test if the game detects a draw scenario properly."""
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)]
        for i, (row, col) in enumerate(moves):
            self.game.play_turn(row, col)
        self.assertFalse(self.game.board.has_won(self.game.player1.symbol))
        self.assertFalse(self.game.board.has_won(self.game.player2.symbol))
        self.assertTrue(self.game.is_draw())

    def test_turn_switching(self):
        """Test if turns switch correctly between players."""
        first_player = self.game.current_player
        self.game.play_turn(1, 1)
        self.assertNotEqual(first_player, self.game.current_player)

    def test_reset_game(self):
        """Test if the game resets properly."""
        self.game.play_turn(0, 0)
        self.game.play_turn(1, 1)
        self.game.reset_game()
        self.assertTrue(self.game.board.is_valid_move(0, 0))
        self.assertTrue(self.game.board.is_valid_move(1, 1))
        self.assertEqual(
            self.game.current_player, self.game.player1
        )  # Assuming Player 1 always starts


if __name__ == "__main__":
    unittest.main()

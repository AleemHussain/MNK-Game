import sys
import os
import random
import numpy as np

# Add parent directory to system path to allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Player import Player  # Import Player class


class MyBot(Player):
    """
    AI Bot with different difficulty levels using Minimax & Alpha-Beta Pruning.

    Difficulty Modes:
        - Mode 1: Random moves.
        - Mode 2: Tries to win immediately or block the opponent.
        - Mode 3: Advanced Minimax AI with board evaluation.
    """

    def make_move(self, current_player, board, mode):
        """
        Determines the bot's next move based on the selected mode.

        :param current_player: The bot's player number (1 or 2).
        :param board: The game board.
        :param mode: Difficulty mode (1 = Random, 2 = Smart blocking, 3 = Minimax AI).
        :return: A tuple (row, col) representing the chosen move.
        """
        # Get all available (empty) positions on the board
        available_moves = [
            (row, col)
            for row in range(board.rows)
            for col in range(board.cols)
            if board.grid[row, col] == 0
        ]

        if not available_moves:
            return None  # No available moves

        if mode == 1:
            return random.choice(available_moves)  # Random move

        # Mode 2: Check for an immediate win or block opponent's win
        for row, col in available_moves:
            board.grid[row, col] = current_player
            if board.has_won(current_player):  # Check if the move results in a win
                board.grid[row, col] = 0  # Undo move
                return row, col
            board.grid[row, col] = 0  # Undo move

        # Block opponent's immediate win
        opponent = 1 if current_player == 2 else 2
        for row, col in available_moves:
            board.grid[row, col] = opponent
            if board.has_won(opponent):  # If opponent is about to win, block them
                board.grid[row, col] = 0  # Undo move
                return row, col
            board.grid[row, col] = 0  # Undo move

        # Mode 3: Use Minimax AI with Alpha-Beta Pruning
        if mode == 3:
            empty_spaces = sum(sum(board.grid == 0))
            depth = self.get_dynamic_depth(empty_spaces)  # Adjust depth dynamically
            _, best_move = self.minimax(board, current_player, True, -np.inf, np.inf, depth)
            return best_move

        return random.choice(available_moves)  # Fallback to random if no better move is found

    def get_dynamic_depth(self, empty_spaces):
        """
        Adjusts search depth dynamically based on remaining empty spaces.

        :param empty_spaces: Number of empty spaces on the board.
        :return: The appropriate depth level for the Minimax search.
        """
        if empty_spaces > 12:
            return 4  # Early game: Shallow search
        elif empty_spaces > 6:
            return 6  # Mid-game: Medium depth
        else:
            return 8  # Endgame: Deep search

    def minimax(self, board, player, maximizing, alpha, beta, depth):
        """
        Implements the Minimax algorithm with Alpha-Beta Pruning.

        :param board: The game board.
        :param player: The current player.
        :param maximizing: True if maximizing, False if minimizing.
        :param alpha: Alpha value for pruning.
        :param beta: Beta value for pruning.
        :param depth: Search depth.
        :return: Best score and best move (row, col).
        """
        opponent = 1 if player == 2 else 2
        available_moves = [
            (row, col)
            for row in range(board.rows)
            for col in range(board.cols)
            if board.grid[row, col] == 0
        ]

        if depth == 0 or not available_moves:
            return self.evaluate_board(board, player), None  # Return board score

        if maximizing:
            best_value = -np.inf
            best_move = None
            for row, col in available_moves:
                board.grid[row, col] = player
                if board.has_won(player):  # Winning move
                    board.grid[row, col] = 0
                    return 10000, (row, col)
                value, _ = self.minimax(board, opponent, False, alpha, beta, depth - 1)
                board.grid[row, col] = 0  # Undo move

                if value > best_value:
                    best_value, best_move = value, (row, col)
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break  # Pruning

            return best_value, best_move

        else:  # Minimizing opponent's moves
            best_value = np.inf
            best_move = None
            for row, col in available_moves:
                board.grid[row, col] = opponent
                if board.has_won(opponent):  # Losing move
                    board.grid[row, col] = 0
                    return -10000, (row, col)
                value, _ = self.minimax(board, player, True, alpha, beta, depth - 1)
                board.grid[row, col] = 0  # Undo move

                if value < best_value:
                    best_value, best_move = value, (row, col)
                beta = min(beta, best_value)
                if beta <= alpha:
                    break  # Pruning

            return best_value, best_move

    def evaluate_board(self, board, player):
        """
        Evaluates the board position for the given player.

        :param board: The game board.
        :param player: The player's number.
        :return: The evaluation score.
        """
        opponent = 1 if player == 2 else 2
        score = 0

        # Control of the center
        center_col = board.cols // 2
        center_row = board.rows // 2
        if board.grid[center_row, center_col] == player:
            score += 50
        elif board.grid[center_row, center_col] == opponent:
            score -= 50

        # Winning and blocking moves
        for row in range(board.rows):
            for col in range(board.cols):
                if board.grid[row, col] == player:
                    score += self.count_potential_wins(board, row, col, player)
                elif board.grid[row, col] == opponent:
                    score -= self.count_potential_wins(board, row, col, opponent)

        return score

    def count_potential_wins(self, board, row, col, player):
        """
        Evaluates how close a player is to winning at a given position.

        :param board: The game board.
        :param row: Row index.
        :param col: Column index.
        :param player: The player's number.
        :return: A score based on potential winning moves.
        """
        opponent = 1 if player == 2 else 2
        score = 0
        winning_potential = 50  # Reward for nearly winning positions

        # Check horizontal segment
        if col <= board.cols - board.k:
            segment = board.grid[row, col : col + board.k]
            if np.count_nonzero(segment == player) == board.k - 1 and np.count_nonzero(segment == 0) == 1:
                score += winning_potential
            elif np.count_nonzero(segment == opponent) == board.k - 1 and np.count_nonzero(segment == 0) == 1:
                score -= winning_potential

        # Check vertical segment
        if row <= board.rows - board.k: 
            segment = board.grid[row : row + board.k, col] 
            if np.count_nonzero(segment == player) == board.k - 1 and np.count_nonzero(segment == 0) == 1:
                score += winning_potential
            elif np.count_nonzero(segment == opponent) == board.k - 1 and np.count_nonzero(segment == 0) == 1:
                score -= winning_potential

        return score

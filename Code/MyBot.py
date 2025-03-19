import sys
import os
import random
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Player import Player

class MyBot(Player):
    """
    AI Bot with Minimax & Alpha-Beta Pruning.
    Difficulty Modes:
        - Mode 1: Random
        - Mode 2: Try to win & block
        - Mode 3: Strong Minimax AI with evaluation
    """

    def make_move(self, current_player, board, mode):
        available_moves = [
            (row, col)
            for row in range(board.rows)  # Fixed `board.m` → `board.rows`
            for col in range(board.cols)  # Fixed `board.n` → `board.cols`
            if board.grid[row, col] == 0  # Fixed `board.array` → `board.grid`
        ]

        if not available_moves:
            return None  # No available moves

        if mode == 1:
            return random.choice(available_moves)

        # Mode 2: Try to win OR block opponent's win
        for row, col in available_moves:
            board.grid[row, col] = current_player
            if board.has_won(current_player):  # Adjusted to new `has_won()`
                board.grid[row, col] = 0  # Undo move
                return row, col
            board.grid[row, col] = 0  # Undo move

        # Block opponent's immediate win
        opponent = 1 if current_player == 2 else 2
        for row, col in available_moves:
            board.grid[row, col] = opponent
            if board.has_won(opponent):
                board.grid[row, col] = 0  # Undo move
                return row, col
            board.grid[row, col] = 0  # Undo move

        # Mode 3: Advanced Minimax AI
        if mode == 3:
            empty_spaces = sum(sum(board.grid == 0))  # Fixed `board.array` → `board.grid`
            depth = self.get_dynamic_depth(empty_spaces)
            _, best_move = self.minimax(
                board, current_player, True, -np.inf, np.inf, depth
            )
            return best_move

        return random.choice(available_moves)

    def get_dynamic_depth(self, empty_spaces):
        """Dynamically adjust depth based on game phase."""
        if empty_spaces > 12:
            return 4  # Early game
        elif empty_spaces > 6:
            return 6  # Mid-game
        else:
            return 8  # Endgame (higher depth)

    def minimax(self, board, player, maximizing, alpha, beta, depth):
        opponent = 1 if player == 2 else 2
        available_moves = [
            (row, col)
            for row in range(board.rows)  # Fixed `board.m` → `board.rows`
            for col in range(board.cols)  # Fixed `board.n` → `board.cols`
            if board.grid[row, col] == 0  # Fixed `board.array` → `board.grid`
        ]

        if depth == 0 or not available_moves:
            return self.evaluate_board(board, player), None

        if maximizing:
            best_value = -np.inf
            best_move = None
            for row, col in available_moves:
                board.grid[row, col] = player
                if board.has_won(player):
                    board.grid[row, col] = 0
                    return 10000, (row, col)  # Immediate win
                value, _ = self.minimax(board, opponent, False, alpha, beta, depth - 1)
                board.grid[row, col] = 0  # Undo move

                if value > best_value:
                    best_value, best_move = value, (row, col)
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break  # Alpha-beta pruning

            return best_value, best_move

        else:  # Minimizing opponent's moves
            best_value = np.inf
            best_move = None
            for row, col in available_moves:
                board.grid[row, col] = opponent
                if board.has_won(opponent):
                    board.grid[row, col] = 0
                    return -10000, (row, col)  # Immediate loss
                value, _ = self.minimax(board, player, True, alpha, beta, depth - 1)
                board.grid[row, col] = 0  # Undo move

                if value < best_value:
                    best_value, best_move = value, (row, col)
                beta = min(beta, best_value)
                if beta <= alpha:
                    break  # Alpha-beta pruning

            return best_value, best_move

    def evaluate_board(self, board, player):
        """Improved heuristic evaluation with winning potential detection."""
        opponent = 1 if player == 2 else 2
        score = 0

        # Center Control
        center_col = board.cols // 2  # Fixed `board.n` → `board.cols`
        center_row = board.rows // 2  # Fixed `board.m` → `board.rows`
        if board.grid[center_row, center_col] == player:
            score += 50
        elif board.grid[center_row, center_col] == opponent:
            score -= 50

        # Winning & Blocking Moves
        for row in range(board.rows):  # Fixed `board.m` → `board.rows`
            for col in range(board.cols):  # Fixed `board.n` → `board.cols`
                if board.grid[row, col] == player:
                    score += self.count_potential_wins(board, row, col, player)
                elif board.grid[row, col] == opponent:
                    score -= self.count_potential_wins(board, row, col, opponent)

        return score

    def count_potential_wins(self, board, row, col, player):
        """Counts how close a player is to winning in a given position."""
        opponent = 1 if player == 2 else 2
        score = 0
        winning_potential = 50  # Reward for almost winning

        # Horizontal check
        if col <= board.cols - board.k:  # Fixed `board.n` → `board.cols`
            segment = board.grid[row, col : col + board.k]  # Fixed `board.array` → `board.grid`
            if (
                np.count_nonzero(segment == player) == board.k - 1
                and np.count_nonzero(segment == 0) == 1
            ):
                score += winning_potential
            elif (
                np.count_nonzero(segment == opponent) == board.k - 1
                and np.count_nonzero(segment == 0) == 1
            ):
                score -= winning_potential

        # Vertical check
        if row <= board.rows - board.k:  # Fixed `board.m` → `board.rows`
            segment = board.grid[row : row + board.k, col]  # Fixed `board.array` → `board.grid`
            if (
                np.count_nonzero(segment == player) == board.k - 1
                and np.count_nonzero(segment == 0) == 1
            ):
                score += winning_potential
            elif (
                np.count_nonzero(segment == opponent) == board.k - 1
                and np.count_nonzero(segment == 0) == 1
            ):
                score -= winning_potential

        return score

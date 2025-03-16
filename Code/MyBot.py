from Player import Player
import random
import numpy as np


class MyBot(Player):
    """
    This class represents an AI bot that inherits from the Player class.
    The `mode` parameter determines the bot's difficulty level.
    """

    def make_move(self, current_player, board, mode):
        """
        Determines the bot's move based on the selected difficulty mode.
        Mode 1: Random move
        Mode 2: Try to win
        Mode 3: Strong Minimax AI with deep evaluation.
        """

        available_moves = [
            (row, col)
            for row in range(board.m)
            for col in range(board.n)
            if board.array[row, col] == 0
        ]

        if not available_moves:
            return None  # No available moves

        if mode == 1:
            return random.choice(available_moves)

        # Mode 2: Try to win immediately
        for row, col in available_moves:
            board.array[row, col] = current_player
            if board.has_won(row, col, current_player):
                board.array[row, col] = 0  # Undo move
                return row, col
            board.array[row, col] = 0  # Undo move

        # Mode 3: Advanced Minimax AI
        if mode == 3:
            # Determine dynamic depth (increases depth as the board fills)
            empty_spaces = sum(sum(board.array == 0))
            depth = 6 if empty_spaces > 10 else 8  # Adjust based on game phase

            _, best_move = self.minimax(
                board, current_player, True, -np.inf, np.inf, depth
            )
            return best_move

        return random.choice(available_moves)

    def minimax(self, board, player, maximizing, alpha, beta, depth):
        """
        Minimax algorithm with Alpha-Beta pruning and strategic heuristics.
        Looks ahead multiple moves to make the best decision.
        """
        opponent = 1 if player == 2 else 2
        available_moves = [
            (row, col)
            for row in range(board.m)
            for col in range(board.n)
            if board.array[row, col] == 0
        ]

        if depth == 0 or not available_moves:
            return self.evaluate_board(board, player), None

        if maximizing:
            best_value = -np.inf
            best_move = None
            for row, col in available_moves:
                board.array[row, col] = player
                if board.has_won(row, col, player):
                    board.array[row, col] = 0
                    return 10000, (row, col)  # Immediate win
                value, _ = self.minimax(board, opponent, False, alpha, beta, depth - 1)
                board.array[row, col] = 0  # Undo move

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
                board.array[row, col] = opponent
                if board.has_won(row, col, opponent):
                    board.array[row, col] = 0
                    return -10000, (row, col)  # Immediate loss
                value, _ = self.minimax(board, player, True, alpha, beta, depth - 1)
                board.array[row, col] = 0  # Undo move

                if value < best_value:
                    best_value, best_move = value, (row, col)
                beta = min(beta, best_value)
                if beta <= alpha:
                    break  # Alpha-beta pruning

            return best_value, best_move

    def evaluate_board(self, board, player):
        """
        Heuristic evaluation for board state.
        Assigns points based on positioning, winning potential, and blocking threats.
        """
        opponent = 1 if player == 2 else 2
        score = 0

        # 1. **Center Control (Highest Priority)**
        center_col = board.n // 2
        center_row = board.m // 2
        center_bonus = 50
        if board.array[center_row, center_col] == player:
            score += center_bonus
        elif board.array[center_row, center_col] == opponent:
            score -= center_bonus

        # 2. **Winning & Blocking Moves**
        for row in range(board.m):
            if sum(board.array[row, :] == player) >= board.k - 1:
                score += 100  # Almost winning row
            if sum(board.array[:, row] == player) >= board.k - 1:
                score += 100  # Almost winning column

        for row in range(board.m):
            if sum(board.array[row, :] == opponent) >= board.k - 1:
                score -= 120  # Opponent close to winning
            if sum(board.array[:, row] == opponent) >= board.k - 1:
                score -= 120  # Opponent close to winning

        # 3. **Forks (Two Winning Moves at Once)**
        fork_bonus = 150
        for row, col in zip(range(board.m), range(board.n)):  # Check diagonals
            if board.array[row, col] == player:
                score += fork_bonus
            if board.array[row, col] == opponent:
                score -= fork_bonus

        # 4. **Chain Building (Preparing for Wins)**
        chain_bonus = 30
        for row in range(board.m):
            for col in range(board.n - board.k + 1):
                segment = board.array[row, col : col + board.k]
                if (
                    np.count_nonzero(segment == player) == board.k - 2
                    and np.count_nonzero(segment == 0) == 2
                ):
                    score += chain_bonus  # Two in a row with space for more

        for col in range(board.n):
            for row in range(board.m - board.k + 1):
                segment = board.array[row : row + board.k, col]
                if (
                    np.count_nonzero(segment == player) == board.k - 2
                    and np.count_nonzero(segment == 0) == 2
                ):
                    score += chain_bonus

        return score

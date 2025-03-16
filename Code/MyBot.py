from Player import Player
import random


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
        Mode 3: Try to win or block opponent's winning move
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

        # Mode 2 and 3: Check for a winning move
        for row, col in available_moves:
            board.array[row, col] = current_player
            if board.has_won(row, col, current_player):
                board.array[row, col] = 0  # Undo move
                return row, col
            board.array[row, col] = 0  # Undo move

        if mode == 3:
            # Check if the opponent has a winning move and block it
            opponent = 1 if current_player == 2 else 2
            for row, col in available_moves:
                board.array[row, col] = opponent
                if board.has_won(row, col, opponent):
                    board.array[row, col] = 0  # Undo move
                    return row, col
                board.array[row, col] = 0  # Undo move

        # If no winning or blocking move is found, choose randomly
        return random.choice(available_moves)

import sys
import os

# Add the parent directory to the system path to allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from Code.Player import Player  # Import Player class
from Code.Board import Board  # Import Board class
from Code.MyBot import MyBot  # Import MyBot class (AI Player)


class Game:
    """
    Represents the game logic for the MNK game.
    This class initializes the board and manages the turns between players.
    """

    def __init__(self, rows, cols, k, player1, player2):
        """
        Initializes the game with a board and two players.

        :param rows: Number of rows in the board.
        :param cols: Number of columns in the board.
        :param k: Number of consecutive marks needed to win.
        :param player1: First player (can be human or bot).
        :param player2: Second player (can be human or bot).
        """
        self.board = Board(rows, cols, k)  # Create the board
        self.player1 = player1  # Assign player 1
        self.player2 = player2  # Assign player 2

    def game_loop(self):
        """
        Runs the main game loop.
        Alternates between players until there is a winner or the game ends in a draw.
        """
        current_player = self.player1  # Start with player 1
        move_count = 0  # Track the number of moves made
        total_moves = (
            self.board.rows * self.board.cols
        )  # Maximum possible moves before a draw

        while move_count < total_moves:
            self.board.display()  # Display the current board state

            # Determine move based on player type (human or bot)
            if isinstance(current_player, MyBot):
                row, col = current_player.make_move(
                    current_player.number, self.board, current_player.mode
                )  # AI move based on difficulty mode
            else:
                row, col = current_player.make_move(
                    current_player.number, self.board
                )  # Human move

            self.board.grid[row, col] = (
                current_player.number
            )  # Place the player's mark on the board

            # Check if the current player has won
            if self.board.has_won(current_player.number):
                self.board.display()  # Display final board state
                print(f"{current_player.name} wins!")  # Announce the winner
                return

            # Switch to the next player
            current_player = (
                self.player2 if current_player == self.player1 else self.player1
            )
            move_count += 1  # Increment move counter

        # If all moves are used and no winner, it's a draw
        self.board.display()
        print("Game ended in a draw.")

    def start(self):
        """Starts the game by entering the game loop."""
        self.game_loop()


def welcome_screen():
    """
    Displays the welcome screen and sets up the game.
    Prompts the user for game configurations and initializes the game accordingly.
    """
    print("\n ------------------------------")
    print("|                              |")
    print("|         M,N,K GAME           |")
    print("|                              |")
    print(" ------------------------------\n")

    print("Game Setup:")
    rows = int(input("\t  Rows: "))  # Get board row size
    cols = int(input("\t  Columns: "))  # Get board column size
    k = int(input("\t  Winning condition (k): "))  # Get win condition (k in a row)

    print("\nGame Modes:")
    print("\t  1 - Player vs Player")
    print("\t  2 - Player vs Bot")
    print("\t  3 - Bot vs Bot")

    game_mode = input("\t  Choose mode (1/2/3): ")  # Get user choice for game mode

    # Configure players based on selected game mode
    if game_mode == "1":
        # Human vs Human mode
        player1 = Player(input("Player 1 name: "), 1, 0)
        player2 = Player(input("Player 2 name: "), 2, 0)

    elif game_mode == "2":
        # Human vs Bot mode
        player1 = Player(input("Player name: "), 1, 0)
        bot_level = int(
            input("Bot difficulty (1 - Easy, 2 - Medium, 3 - Hard): ")
        )  # Choose bot difficulty
        player2 = MyBot(f"Bot Level {bot_level}", 2, bot_level)

    elif game_mode == "3":
        # Bot vs Bot mode
        bot1_level = int(
            input("First bot difficulty (1 - Easy, 2 - Medium, 3 - Hard): ")
        )
        bot2_level = int(
            input("Second bot difficulty (1 - Easy, 2 - Medium, 3 - Hard): ")
        )
        player1 = MyBot(f"Bot Level {bot1_level}", 1, bot1_level)
        player2 = MyBot(f"Bot Level {bot2_level}", 2, bot2_level)

    else:
        print("Invalid selection. Exiting.")  # Handle invalid input
        exit()

    # Start the game with configured players
    game = Game(rows, cols, k, player1, player2)
    game.start()


if __name__ == "__main__":
    """
    Entry point of the script. Runs the game setup when executed.
    """
    welcome_screen()

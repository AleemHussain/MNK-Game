from Player import Player
from Board import Board
from MyBot import MyBot


class Game:
    """
    This class represents the game logic. It initializes a board and two players.
    """

    def __init__(self, rows, cols, k, player1, player2):
        self.board = Board(rows, cols, k)
        self.player1 = player1
        self.player2 = player2

    def game_loop(self):
        """
        Runs the main game loop, alternating between players until a win or a draw occurs.
        """
        current_player = self.player1
        move_count = 0
        total_moves = self.board.rows * self.board.cols  # Fixed attribute names

        while move_count < total_moves:
            self.board.display()

            # Check if the current player is a bot
            if isinstance(current_player, MyBot):
                row, col = current_player.make_move(
                    current_player.number, self.board, current_player.mode
                )
            else:
                row, col = current_player.make_move(current_player.number, self.board)

            self.board.grid[row, col] = current_player.number  # Fixed `array` → `grid`

            # Check if the current player has won
            if self.board.has_won(current_player.number):  # Fixed call
                self.board.display()
                print(f"{current_player.name} wins!")
                return

            # Switch player
            current_player = (
                self.player2 if current_player == self.player1 else self.player1
            )
            move_count += 1

        # If no winner and board is full, it's a draw
        self.board.display()
        print("Game ended in a draw.")

    def start(self):
        """Starts the game loop."""
        self.game_loop()


def welcome_screen():
    print("\n ------------------------------")
    print("|                              |")
    print("|         M,N,K GAME           |")
    print("|                              |")
    print(" ------------------------------\n")

    print("Game Setup:")
    rows = int(input("\t  Rows: "))  # Fixed `m` → `rows`
    cols = int(input("\t  Columns: "))  # Fixed `n` → `cols`
    k = int(input("\t  Winning condition (k): "))

    print("\nGame Modes:")
    print("\t  1 - Player vs Player")
    print("\t  2 - Player vs Bot")
    print("\t  3 - Bot vs Bot")

    game_mode = input("\t  Choose mode (1/2/3): ")

    if game_mode == "1":
        player1 = Player(input("Player 1 name: "), 1, 0)
        player2 = Player(input("Player 2 name: "), 2, 0)

    elif game_mode == "2":
        player1 = Player(input("Player name: "), 1, 0)
        bot_level = int(input("Bot difficulty (1 - Easy, 2 - Medium, 3 - Hard): "))
        player2 = MyBot(f"Bot Level {bot_level}", 2, bot_level)

    elif game_mode == "3":
        bot1_level = int(
            input("First bot difficulty (1 - Easy, 2 - Medium, 3 - Hard): ")
        )
        bot2_level = int(
            input("Second bot difficulty (1 - Easy, 2 - Medium, 3 - Hard): ")
        )
        player1 = MyBot(f"Bot Level {bot1_level}", 1, bot1_level)
        player2 = MyBot(f"Bot Level {bot2_level}", 2, bot2_level)

    else:
        print("Invalid selection. Exiting.")
        exit()

    game = Game(rows, cols, k, player1, player2)  # Fixed `m, n` → `rows, cols`
    game.start()


if __name__ == "__main__":
    welcome_screen()

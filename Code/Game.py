from Player import Player
from Board import Board
from MyBot import MyBot


class Game:
    """
    This class represents the game logic. It initializes a board and two players.
    """

    def __init__(self, m, n, k, player1, player2):
        self.board = Board(m, n, k)
        self.player1 = player1
        self.player2 = player2

    def game_loop(self):
        """
        Runs the main game loop, alternating between players until a win or a draw occurs.
        """
        current_player = self.player1
        move_count = 0
        total_moves = self.board.m * self.board.n

        while move_count < total_moves:
            self.board.display()

            # Check if the current player is a bot
            if isinstance(current_player, MyBot):
                row, col = current_player.make_move(
                    current_player.number, self.board, current_player.mode
                )
            else:
                row, col = current_player.make_move(current_player.number, self.board)

            self.board.array[row, col] = current_player.number

            # Check if the current player has won
            if self.board.has_won(row, col, current_player.number):
                self.board.display()
                print(f"{current_player.name} has won!")
                return

            # Switch player
            current_player = (
                self.player2 if current_player == self.player1 else self.player1
            )
            move_count += 1

        # If no winner and board is full, it's a draw
        self.board.display()
        print("The game is a draw!")

    def start(self):
        """
        Starts the game loop.
        """
        self.game_loop()


# Game Setup
print("Welcome to the M,N,K game! To start, please enter the following:")
m = int(input("Number of rows: "))
n = int(input("Number of columns: "))
k = int(input("Winning condition (k): "))

# Select Game Mode
print("Select Game Mode: \n1. Player vs Player \n2. Player vs Bot \n3. Bot vs Bot")
game_mode = input("Enter mode (1/2/3): ")

if game_mode == "1":
    player1_name = input("Player 1, enter your name: ")
    player1 = Player(player1_name, 1, 0)

    player2_name = input("Player 2, enter your name: ")
    player2 = Player(player2_name, 2, 0)

elif game_mode == "2":
    player1_name = input("Player 1, enter your name: ")
    player1 = Player(player1_name, 1, 0)

    bot_level = int(
        input("Select bot level: \n1. Random Bot \n2. Level 2 Bot \n3. Level 3 Bot\n")
    )
    player2 = MyBot(f"Bot Level {bot_level}", 2, bot_level)

elif game_mode == "3":
    bot1_level = int(
        input(
            "Select first bot level: \n1. Random Bot \n2. Level 2 Bot \n3. Level 3 Bot\n"
        )
    )
    player1 = MyBot(f"Bot Level {bot1_level}", 1, bot1_level)

    bot2_level = int(
        input(
            "Select second bot level: \n1. Random Bot \n2. Level 2 Bot \n3. Level 3 Bot\n"
        )
    )
    player2 = MyBot(f"Bot Level {bot2_level}", 2, bot2_level)

else:
    print("Invalid choice. Exiting the game.")
    exit()

# Start Game
game = Game(m, n, k, player1, player2)
game.start()

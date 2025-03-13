class Player:
    """
    This class represents a player in the game.
    The `mode` parameter is used for the MyBot class but has no function here.
    """

    def __init__(self, name, number, mode):
        self.name = name
        self.number = number
        self.mode = mode

    def make_move(self, current_player_number, board):
        """
        Asks the player for a valid move and returns the coordinates.
        Ensures that the input is valid and the selected position is free.
        """

        while True:
            try:
                row = int(input(f"{self.name}, choose a row (1-{board.m}): ")) - 1
                col = int(input(f"{self.name}, choose a column (1-{board.n}): ")) - 1

                # Validate the input
                if 0 <= row < board.m and 0 <= col < board.n and board.array[row, col] == 0:
                    return row, col
                else:
                    print("Invalid move! The field is either out of bounds or already occupied. Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
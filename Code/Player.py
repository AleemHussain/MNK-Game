class Player:
    """
    Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        number (int): The player's unique number (1 or 2).
        mode (int): Included for compatibility with MyBot but has no function here.
    """

    def __init__(self, name, number, mode):
        """
        Initializes a player.

        :param name: The player's name.
        :param number: The player's unique identifier (1 or 2).
        :param mode: Not used in this class but required for MyBot compatibility.
        """
        self.name = name
        self.number = number
        self.mode = mode  # Placeholder for compatibility with MyBot

    def make_move(self, current_player_number, board):
        """
        Asks the player for a valid move and returns the coordinates.

        Ensures that:
        - The input is within the board's bounds.
        - The chosen position is not already occupied.

        :param current_player_number: The current player's number (1 or 2).
        :param board: The game board object.
        :return: A tuple (row, col) representing the chosen move.
        """

        while True:
            try:
                # Ask player for input and adjust to zero-based indexing
                row = int(input(f"{self.name}, choose a row (1-{board.rows}): ")) - 1
                col = int(input(f"{self.name}, choose a column (1-{board.cols}): ")) - 1

                # Check if the move is valid
                if (
                    0 <= row < board.rows  # Row is within bounds
                    and 0 <= col < board.cols  # Column is within bounds
                    and board.grid[row, col] == 0  # The cell is unoccupied
                ):
                    return row, col  # Return valid move
                else:
                    print(
                        "Invalid move! The field is either out of bounds or already occupied. Try again."
                    )
            except ValueError:
                print("Invalid input! Please enter a valid number.")

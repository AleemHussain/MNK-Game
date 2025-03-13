# from Player import Player
from Board import Board

# from MyBot import MyBot


class Game:

    def __init__(self, m, n, k, player1, player2):
        self.board = Board(m, n, k)
        self.player1 = player1
        self.player2 = player2

    def game_loop(self):
        pass

    def start(self):
        pass

    pass

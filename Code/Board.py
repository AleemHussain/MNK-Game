import numpy as np


class Board:
    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
        self.array = np.zeros((m, n))

    def display(self):
        pass

    def has_won(self):
        pass

    pass

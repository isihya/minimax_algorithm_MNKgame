import numpy as np
from game import Game


class MNKgame(Game):
    """
    https://en.wikipedia.org/wiki/M,n,k-game
    If m=3, n=3, k=3. This is TicTakToe and default
    """

    def __init__(self, n=3, m=3, k=3, field=None):
        self.n = n
        self.m = m
        self.k = k
        self.field = field
        if field is None:
            self.field = np.zeros((n, m))
        self.winner = 0

    def evaluate(self, field) -> bool:
        # down
        for x in range(self.m):
            score = self.scan(field, (1, 0), 0, x)
            if score != 0:
                return score
        # right
        for y in range(self.n):
            score = self.scan(field, (0, 1), y, 0)
            if score != 0:
                return score
        # right down
        for x in range(self.m):
            score = self.scan(field, (1, 1), 0, x)
            if score != 0:
                return score
        for y in range(self.n):
            score = self.scan(field, (1, 1), y, 0)
            if score != 0:
                return score
        # right up
        for x in range(self.n):
            score = self.scan(field, (-1, 1), self.m, x)
            if score != 0:
                return score
        for y in range(self.m):
            score = self.scan(field, (-1, 1), y, 0)
            if score != 0:
                return score
        return 0

    def scan(self, field, d, i, j) -> bool:
        cnt_player = 0
        cnt_enemy = 0
        while(self.is_in_field(i, j)):
            if int(field[i][j]) == 1:
                cnt_player += 1
                if cnt_player == self.k:
                    return 1
            elif int(field[i][j]) == -1:
                cnt_enemy += 1
                if cnt_enemy == self.k:
                    return -1
            else:
                cnt_player = 0
                cnt_enemy = 0
            i += d[0]
            j += d[1]
        return 0

    def is_in_field(self, i, j):
        if 0 <= i and i < self.n and 0 <= j and j < self.m:
            return True
        return False

    def update(self, action, val):
        self.field[action[0]][action[1]] = val

    def get_actions(self, field):
        indexes = np.where(field == 0)
        if len(indexes[0]) == 0:
            return []
        return list(zip(indexes[0], indexes[1]))

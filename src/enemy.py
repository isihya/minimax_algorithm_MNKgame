import numpy as np


class Enemy:
    def __init__(self, game, val, policy=None, seed=0):
        self.game = game
        self.policy = policy
        self.val = val
        np.random.seed(seed)

    def play(self):
        actions = self.policy.select_action(self.val)
        if len(actions) == 0:
            return
        action = actions[np.random.randint(len(actions))]
        self.game.update(action, self.val)
        if self.game.evaluate(self.game.field) != 0:
            print("Enemy won")
            self.game.winner = -1

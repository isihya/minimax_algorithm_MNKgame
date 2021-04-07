

class Player:
    def __init__(self, game, gametree, val):
        """
        Args: int
            a value which will be filled in field and indicates
            who played certain action (like O and X)
        """
        self.val = val
        self.game = game
        self.gametree = gametree

    def receive_input(self):
        print("Please type next action")
        while True:
            i = input()
            try:
                i = int(i)
            except ValueError:
                print("input should be int. Try again")
                continue
            j = input()
            try:
                j = int(j)
            except ValueError:
                print("input should be int. Try again")
                continue
            if not self.game.is_in_field(i, j):
                print("Selected out of field. Try again")
                continue
            if int(self.game.field[i][j]) != 0:
                print("Already placed. Try again")
                continue
            break
        return (i, j)

    def play(self):
        print(self.game.field)
        action = self.receive_input()
        self.game.update(action, self.val)
        self.gametree.add_node(self.game.field)
        if self.game.evaluate(self.game.field) != 0:
            print("Player won")
            self.game.winner = 1

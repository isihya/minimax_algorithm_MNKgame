

class Minimax_algorithm:
    def __init__(self, game, gametree, depth_lim=-1):
        self.game = game
        self.gametree = gametree
        self.depth_lim = depth_lim

    def select_action(self, val):
        self.explore(self.game.field, val, val == 1,
                     depth_lim=self.depth_lim)
        actions = self.game.get_actions(self.game.field)
        if len(actions) == 0:
            return []
        children = self.gametree.tree[self.game.field.tostring()].children
        act_val = dict(zip(actions,
                           [self.gametree.tree[child.tostring()].value * val
                            for child in children]))
        maxv = max(act_val.values())
        return [action for action, v in act_val.items() if v == maxv]

    def explore(self, field, val, is_my_turn: bool, depth_lim=-1):
        """explore game tree, depth_lim == -1 indicates no limit
        """
        # return if already visited
        if self.gametree.tree[field.tostring()].value is not None:
            return self.gametree.tree[field.tostring()].value
        # get possible actions from current field
        actions = self.game.get_actions(field)
        # if reached limit of explore, return current score
        if depth_lim == 0 or len(actions) == 0:
            score = self.game.evaluate(field)
            return score
        # get child fields
        children = self.gametree.get_children(field, actions, val)
        if is_my_turn:
            score = -2
        else:
            score = 2
        for child in children:
            # if we have cached value of child, use it, else explore
            if self.gametree.tree[child.tostring()].value is not None:
                candidate = child.value
            else:
                candidate = self.explore(
                    child, -1*val, not is_my_turn, depth_lim - 1)
            if is_my_turn:
                score = max(score, candidate)
            else:
                score = min(score, candidate)
        self.gametree.tree[field.tostring()].value = score
        return score

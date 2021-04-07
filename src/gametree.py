from copy import deepcopy


class GameTree:
    def __init__(self, game):
        self.tree = {}
        self.field = game.field
        self.tree[game.field.tostring()] = GameNode(game.field)
        self.game = game

    def get_children(self, field, actions, val):
        field = deepcopy(field)
        children = []
        for action in actions:
            field_updated = deepcopy(field)
            field_updated[action[0]][action[1]] = val
            self.add_node(field_updated)
            children.append(field_updated)
        self.tree[field.tostring()].children = children
        return children

    def add_node(self, field):
        self.tree[field.tostring()] = GameNode(field)


class GameNode:
    def __init__(self, field):
        self.field = field
        self.actions = None
        self.children = None
        self.value = None

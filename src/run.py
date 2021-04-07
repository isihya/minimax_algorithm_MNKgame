from mnkgame import MNKgame
from gametree import GameTree
from player import Player
from enemy import Enemy
from minimax_algorithm import Minimax_algorithm


def main():
    game = MNKgame()
    gametree = GameTree(game)
    minimax_algorithm = Minimax_algorithm(game, gametree)
    me = Player(game, gametree, 1)
    enemy = Enemy(game, -1, policy=minimax_algorithm)
    turn = 0
    is_player_first = True
    while turn < game.n * game.m:
        if is_player_first:
            me.play()
            if game.winner != 0:
                break
            enemy.play()
        else:
            enemy.play()
            if game.winner != 0:
                break
            me.play()
        if game.winner != 0:
            break
        turn += 2
    if game.winner == 0:
        print("DRAW GAME")


if __name__ == "__main__":
    main()

from mnkgame import MNKgame
from gametree import GameTree
from player import Player
from enemy import Enemy
from minimax_algorithm import Minimax_algorithm
import argparse


def main(m, n, k, depth_lim):
    game = MNKgame(m=m, n=n, k=k)
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
    parser = argparse.ArgumentParser(description='MNKgame')
    parser.add_argument('--m', type=int, default=3,
                        help='width of board')
    parser.add_argument('--n', type=int, default=3,
                        help='height of board')
    parser.add_argument('--k', type=int, default=3,
                        help='player who first gets'
                             'k stones in a row will win')
    parser.add_argument('--l', type=int, default=5,
                        help='depth whih enemy will explore')
    args = parser.parse_args()
    main(args.m, args.n, args.k, args.l)

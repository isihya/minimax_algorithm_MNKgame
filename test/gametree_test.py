import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from minimax_algorithm import Minimax_algorithm
from enemy import Enemy
from player import Player
from gametree import GameTree
from mnkgame import MNKgame
import numpy as np


def test_game_evaluate_field():
    game = MNKgame()
    field1 = [[1, 1, 1],
              [0, 0, 0],
              [0, 0, 0]]
    assert game.evaluate(field1) == 1
    field2 = [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]
    assert game.evaluate(field2) == 1
    field3 = [[1, 0, 0],
              [1, 0, 0],
              [1, 0, 0]]
    assert game.evaluate(field3) == 1
    field4 = [[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]]
    assert game.evaluate(field4) == 1
    field5 = [[0, 0, 0],
              [-1, 1, 0],
              [1, 0, 0]]
    assert game.evaluate(field5) == 0
    field6 = [[0, 0, 0],
              [-1, 1, 1],
              [0, 0, 0]]
    assert game.evaluate(field6) == 0
    field7 = [[0, 0, 0],
              [-1, -1, -1],
              [0, 0, 0]]
    assert game.evaluate(field7) == -1


def test_minmax_algorithm_chose_win():
    field = [[1, -1, -1],
             [1, 1, 0],
             [-1, -1, 0]]
    game = MNKgame(field=np.array(field))
    gametree = GameTree(game)
    minimax_algo = Minimax_algorithm(game, gametree)
    enemy = Enemy(game, -1, policy=minimax_algo)
    enemy.play()
    print(game.field)
    field_out = [[1, -1, -1],
                 [1, 1, 0],
                 [-1, -1, -1]]
    assert np.array_equal(game.field, field_out)


def test_minmax_algorithm_prevent_lose():
    field = [[1, -1, 0],
             [0, 1, 0],
             [0, -1, 0]]
    game = MNKgame(field=np.array(field))
    gametree = GameTree(game)
    minimax_algo = Minimax_algorithm(game, gametree)
    enemy = Enemy(game, -1, policy=minimax_algo)
    enemy.play()
    print(game.field)
    field_out = [[1, -1, 0],
                 [0, 1, 0],
                 [0, -1, -1]]
    assert np.array_equal(game.field, field_out)


def test_minmax_algorithm_play_optimal_game():
    field = [[1, -1, 0],
             [0, 1, 0],
             [0, -1, 0]]
    game = MNKgame(field=np.array(field))
    gametree = GameTree(game)
    minimax_algo = Minimax_algorithm(game, gametree)
    enemy = Enemy(game, -1, policy=minimax_algo)
    enemy2 = Enemy(game, 1, policy=minimax_algo)
    enemy.play()
    field_out = [[1, -1, 0],
                 [0, 1, 0],
                 [0, -1, -1]]
    assert np.array_equal(game.field, field_out)
    enemy2.play()
    field_out = [[1, -1, 0],
                 [0, 1, 0],
                 [1, -1, -1]]
    assert np.array_equal(game.field, field_out)
    enemy.play()
    field_out = [[1, -1, -1],
                 [0, 1, 0],
                 [1, -1, -1]]
    assert np.array_equal(game.field, field_out)
    enemy2.play()
    field_out = [[1, -1, -1],
                 [1, 1, 0],
                 [1, -1, -1]]
    assert np.array_equal(game.field, field_out)


def test_game_will_finish():
    field = [[1, -1, -1],
             [1, 1, 0],
             [-1, -1, 0]]
    game = MNKgame(field=np.array(field))
    gametree = GameTree(game)
    minimax_algo = Minimax_algorithm(game, gametree)
    enemy = Enemy(game, -1, policy=minimax_algo)
    enemy.play()
    assert game.winner == -1


def test_player_place_piece(mocker):
    field = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    game = MNKgame(field=np.array(field))
    gametree = GameTree(game)
    player = Player(game, gametree, 1)
    mocker.patch("player.Player.receive_input", return_value=(0, 0))
    player.play()
    field_out = [[1, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    assert np.array_equal(game.field, field_out)


def test_enemy_cannot_place():
    field = [[-1, 1, -1],
             [1, -1, 1],
             [-1, 1, -1]]
    game = MNKgame(field=np.array(field))
    gametree = GameTree(game)
    minimax_algo = Minimax_algorithm(game, gametree)
    enemy = Enemy(game, -1, policy=minimax_algo)
    enemy.play()

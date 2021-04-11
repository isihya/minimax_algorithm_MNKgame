# minimax_algorithm_MNKgame
Implementation of m,n,k-game (generalized Tic-Tac-Toe) and minimax_algorithm.

## How to play
`python3 src/run.py`

```
usage: run.py [-h] [--m M] [--n N] [--k K] [--l L]

optional arguments:
  -h, --help  show this help message and exit
  --m M       width of board
  --n N       height of board
  --k K       player who first gets k stones in a row will win
  --l L       depth whih enemy will explore
```

## Demo

For each turn, type pos of your stone (1 in board).
You'll see enemy's feedback after that.

```
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
Please type next action
Type vertical pos
1
Type horizontal pos
1
[[ 0.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.]
 [ 0.  0.  0. -1.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]]
Please type next action
Type vertical pos
2
Type horizontal pos
2
[[ 0.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.]
 [ 0.  0.  1. -1.  0.]
 [ 0.  0.  0. -1.  0.]
 [ 0.  0.  0.  0.  0.]]
```

## How to run test
`pytest -sv test`

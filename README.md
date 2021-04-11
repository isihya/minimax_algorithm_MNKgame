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
  --k K       player who first getsk stones in a row will win
  --l L       depth whih enemy will explore
```

## How to run test
`pytest -sv test`

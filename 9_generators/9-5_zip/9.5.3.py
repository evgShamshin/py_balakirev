import sys

lst_in = list(map(str.split, sys.stdin.readlines()))

[print(*i) for i in zip(*lst_in)]
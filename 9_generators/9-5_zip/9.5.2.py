import sys

def min_len(lst):
    min_len = sys.maxsize
    for l in lst:
        if len(l) < min_len: min_len = len(l)
    return min_len


lst_in = list(map(str.split, sys.stdin.readlines()))
print(list(zip(*zip(*lst_in))))
min = min_len(lst_in)
[print(*i[:min]) for i in lst_in]   
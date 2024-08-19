import sys

def check_len(l):
    return [j for j in ([i.split() for i in l]) if len(j) == 1]

books = list(map(str.strip, sys.stdin.readlines()))
res = check_len(books)
[print(*i, end=" ") for i in res]
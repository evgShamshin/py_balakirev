import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_out = tuple(tuple(i.split("=")) for i in lst_in)
things = filter(lambda x: int(x[1]) > 500, lst_out)
print(*(thing[0] for thing in [*things]))
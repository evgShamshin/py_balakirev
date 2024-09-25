import sys

lst_in = list(map(lambda x: x.strip().split("="), sys.stdin.readlines()))
[print(i[0], end=" ") for i in sorted(lst_in, key=lambda x: -int(x[1]))]
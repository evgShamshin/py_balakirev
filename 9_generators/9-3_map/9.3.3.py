from sys import stdin

lst_in = list(map(str.strip, stdin.readlines()))
lst2D = [list(map(int, i)) for i in list(map(str.split, lst_in))]
print(lst2D)
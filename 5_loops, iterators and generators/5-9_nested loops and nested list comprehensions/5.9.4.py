import sys

res, temp = [], []
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
rows = len(lst_in)
cols = len(lst_in[0])

lst_out = [[lst_in[j][i] for j in range(rows)] for i in range(cols)]

[print(*i) for i in lst_out]
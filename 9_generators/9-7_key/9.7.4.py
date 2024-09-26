import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_out = list(map(lambda x: x.split(";"), lst_in))

for i in range(len(lst_out)):
    for j in range(len(lst_out[i])):
        if (j == 0 or j == 2) and i != 0: lst_out[i][j] = int(lst_out[i][j])


t_sorted = tuple((i[1], i[3], i[2], i[0]) for i in lst_out)

print(t_sorted)
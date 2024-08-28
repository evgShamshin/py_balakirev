import sys


s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

len_1 = len(lst_in)
len_2 = [len(i) for i in lst_in][0]
print(len_1, len_2)

if len_1 > len_2:
    A = [[(i, j) for j in range(len(lst_in[i]))] for i in range(len(lst_in))]
elif len_1 < len_2:
    A = [[(j, i) for j in range(len(lst_in[i]))] for i in range(len(lst_in))]
elif len_1 == len_2:
    A = [[lst_in[j][i] for j in range(len(lst_in[i]))] for i in range(len(lst_in))]

[print(b) for b in A]
print(A)

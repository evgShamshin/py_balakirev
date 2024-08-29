import sys
res = []
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
for i in range(len(lst_in) - 1):
    for j in range(len(lst_in[i]) + 1):
        res.append(lst_in[j][i])

A = [[j for j in range(len(lst_in[i]) + 1)] for i in range(len(lst_in) - 1)]
print(A)
print(res)
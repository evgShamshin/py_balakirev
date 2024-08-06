import sys

# считывание списка из входного потока
lst_in = list(map(str.split, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for i in range(len(lst_in)):
    lst_in[i] = tuple(lst_in[i])

print(tuple(lst_in))
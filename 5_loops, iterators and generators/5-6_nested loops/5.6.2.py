import sys

# считывание списка из входного потока
lst_in = list(map(str.split, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for i in lst_in:
    print(*i, sep="-")
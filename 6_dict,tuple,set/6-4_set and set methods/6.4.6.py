import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
res = set()
for i in lst_in:
    print(lst_in[:i.index(":")])

print("авав".index("в"))
import sys

# считывание списка из входного потока
lst_in = list(map(str.split, sys.stdin.readlines()))
d = {}

# здесь продолжайте программу (используйте список lst_in)
for i in lst_in:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d.setdefault(i[0], []).append(i[1])

for i in d:
    print(i + ":", end = " ")
    print(*d[i], sep=", ")
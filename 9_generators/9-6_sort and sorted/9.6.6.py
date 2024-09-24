import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
res = [i.split(":") for i in lst_in]

[print(i[0], end=" ") for i in sorted(res, key=lambda x: int(x[1]))[:3]]
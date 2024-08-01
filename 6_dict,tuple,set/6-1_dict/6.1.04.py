import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
print(lst_in)
_list = []

for i in lst_in:
    temp_1 = i.split("=")
    temp_2 = []
    temp_2.append(int(temp_1[0]))
    temp_2.append(temp_1[1])
    _list.append(temp_2)

print(_list)
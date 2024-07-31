import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
_dict = {}

for i in lst_in:
    _temp = i.split()
    if _temp[1] in _dict:
        _dict[_temp[1]].append(_temp[0])
    else:
        _dict[_temp[1]] = [_temp[0]]

print(*sorted(_dict.items()))
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

_dict = {}

for _str in lst_in:
    if _str in _dict:
        print("Взято из кэша: HTML-страница для адреса", _dict[_str])
    else:
        _dict[_str] = _str
        print("HTML-страница для адреса", _dict[_str])
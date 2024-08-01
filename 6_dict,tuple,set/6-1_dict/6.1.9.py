from math import sqrt

_dict = {}

while True:
    _number = int(input())
    if _number == 0:
        break
    if _number not in _dict:
        _dict[_number] = round(sqrt(_number),2)
        print(_dict[_number])
    else:
        print("значение из кэша:", _dict[_number])
_list = input().split()
_dict = {}

for i in _list:
    if i[:2] in _dict.keys():
        _temp = _dict[i[:2]]
        _temp.append(i)
        _dict[i[:2]] = _temp
    else:
        _dict[i[:2]] = [i]

print(*sorted(_dict.items()))
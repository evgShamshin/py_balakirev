_list = input().split()
_dict = {}

for i in _list:
    if i not in _dict:
        _dict.setdefault(i)

print(*_dict.keys())
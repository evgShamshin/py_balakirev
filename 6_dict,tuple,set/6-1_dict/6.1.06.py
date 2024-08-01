_list = input().split()
_dict = {}
_list_ignore = ["3", "False"]

for i in _list:
    temp = i.split('=')
    if temp[0] not in _list_ignore:
        _dict[temp[0]] = temp[1]

print(*sorted(_dict.items()))
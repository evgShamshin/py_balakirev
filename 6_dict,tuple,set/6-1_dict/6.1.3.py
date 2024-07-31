_list = input().split()
_dict = {}

for i in _list:
    temp = i.split('=')
    _dict[temp[0]] = int(temp[1])

print(_dict)
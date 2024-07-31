_list = input().split()
_dict = {}
_flag = "НЕТ"
_count = 0

for i in _list:
    temp = i.split("=")
    _dict[temp[0]] = temp[1]

for i in _dict.keys():
    if i in ["house", "True", "5"]:
        _count += 1

if _count == 3:
    _flag = "ДА"

print(_flag)
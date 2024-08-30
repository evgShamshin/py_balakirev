cities = input().split()
_dict = {}

for city in cities:
    _dict[city] = len(city)

a = sorted(_dict, key=_dict.get)
print(*a)
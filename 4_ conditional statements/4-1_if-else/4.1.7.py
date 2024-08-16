cities = input().split()
cities.remove("Москва") if "Москва" in cities else cities
print(*cities)
cities = filter(lambda x: len(x) > 5, input().split())
print(*(next(cities) for _ in range(3)))
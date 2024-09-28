import random

random.seed(1)
a, b = map(int, input().split())
print(round(random.randint(a, b), 2))
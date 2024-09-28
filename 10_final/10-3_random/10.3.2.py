import random

random.seed(1)
a, b = map(float, input().split())
print(round(random.uniform(a, b - 1), 2))
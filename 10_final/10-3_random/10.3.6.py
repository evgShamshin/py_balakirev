import random

random.seed(1)
surname = input().split()
print(*random.sample(surname, 3))
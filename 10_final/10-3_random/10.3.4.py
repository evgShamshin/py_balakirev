import random

towns = input().split()
random.seed(1)
print(random.choice(towns))
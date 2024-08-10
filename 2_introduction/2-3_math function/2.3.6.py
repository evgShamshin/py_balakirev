from math import factorial

# ввод данных
n, k = map(int, input().split())

# здесь продолжите программу
res = factorial(n) / (factorial(k) * factorial(n-k))
print(round(res))
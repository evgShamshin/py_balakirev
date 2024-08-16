c, a, b = list(map(int, input().split()))
print(("НЕТ", "ДА")[c**2 == a**2 + b**2])
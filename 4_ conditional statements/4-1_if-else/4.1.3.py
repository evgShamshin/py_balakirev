m, n = list(map(int, input().split()))
print([f"{m} на {n} нацело не делится", m // n][m % n == 0])
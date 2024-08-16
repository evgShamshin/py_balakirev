a, b, c, d = list(map(int, input().split()))

if (a - 2 >= c and b - 2 >= d) or (b - 2 >= c and a - 2 >= d):
    print("ДА")
else:
    print("НЕТ")
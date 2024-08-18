n, m = list(map(int, input().split()))

for i in range(n, m):
    if i % 2 != 0:
        print(i, end=" ")
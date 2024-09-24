
l = set(map(int, input().split()))
l = sorted(l, reverse=True)[:4]
print(*l)
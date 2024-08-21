l = list(map(float, input().split()))

for i, d in enumerate(l):
    if d < 0:
        l[i] = -1.0

print(*l)
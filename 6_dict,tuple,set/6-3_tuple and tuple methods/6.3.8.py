num = tuple(map(int, input().split()))
res = []

for n in range(len(num)):
    res.append(n) if num.count(num[n]) > 1 else res

print(*res)
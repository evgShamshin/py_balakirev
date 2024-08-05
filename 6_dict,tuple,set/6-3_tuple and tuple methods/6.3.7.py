num_1 = tuple(map(int, input().split()))
res = []
for i in num_1:
    res.append(i) if i not in res else res
res = tuple(res)
print(*res)
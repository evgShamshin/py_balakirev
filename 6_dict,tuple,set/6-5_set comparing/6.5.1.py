set_1 = set(input().split())
set_2 = set(input().split())

res = set_1.intersection(set_2)
print(*sorted(res))
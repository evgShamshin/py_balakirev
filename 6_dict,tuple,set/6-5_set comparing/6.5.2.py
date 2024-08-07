set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))

res = set_1 - set_2
print(*sorted(res))
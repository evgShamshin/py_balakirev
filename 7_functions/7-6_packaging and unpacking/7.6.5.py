lst = list(map(int, input().split()))
print(*[i for i in range(*lst)], lst[1])
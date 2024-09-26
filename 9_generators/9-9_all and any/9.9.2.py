nums = map(float, input().split())
res = any(map(lambda x: x < 0, nums))
print(res)
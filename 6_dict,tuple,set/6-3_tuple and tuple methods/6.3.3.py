t = (3.4, -56.7)
t = list(t)

num = list(map(lambda x: int(x), input().split()))

total = t + num

print(tuple(total))
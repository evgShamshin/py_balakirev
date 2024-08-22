n = int(input())
res = []
temp = []

for _1 in range(n + 1):
    res.append(temp) if temp != [] else 1
    temp = []
    for _2 in range(n):
        temp.append(1)
    temp[-1] = 5

for i in res:
    print(*i)
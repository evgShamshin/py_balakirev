def simple_num(n):
    for i in range(2, n + 1):
        flag = 0
        for j in range(2, i):
            flag += 1 if i % j == 0 else 0
        if flag == 0: yield i


l = []
i = 1
while len(l) < 20:
    i += 1
    l = list(simple_num(i))

print(*l)
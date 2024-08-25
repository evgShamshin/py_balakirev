money = [64, 32, 16, 8, 4, 2, 1]
num = int(input())
res = []
rem = -999

for i in money:
    if num < i:
        continue

    if rem == -999:
        rem = num % i
        res.append([i] * (num // i))
    elif rem > 0:
        if rem % i == 0 and i not in res:
            res.append([i] * (rem // i))
            rem %= i
        elif rem % i == 0 and i in res:
            continue
        else:
            res.append([i] * (rem // i))
            rem %= i

for i in [res for res in res if res]:
    print(*i, end=' ')






num = int(input())

for i in range(1, num + 2):
    if i ** 2 > num:
        res = i
        break
    else:
        res = i

print(res)
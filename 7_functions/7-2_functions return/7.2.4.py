def get_even(n):
    return n if n % 2 == 0 else 999


n = int(input())
res = []
while n != 1:
    res.append(get_even(n))
    n = int(input())

while 999 in res:
    res.remove(999)

print(*res, sep = "\n")
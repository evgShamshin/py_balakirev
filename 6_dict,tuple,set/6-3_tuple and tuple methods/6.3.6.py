t_in = list(map(lambda x: x.lower(), input().split()))

def va(t):
    if "ва" in t:
        return t.lower()

temp = list(map(va, t_in))
total = []

for i in temp:
    if i is not None:
        total.append(i)

print(*total)
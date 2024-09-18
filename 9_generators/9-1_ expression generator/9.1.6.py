a = int(input())

gen = (z ** 3 for z in (abs(x) for x in range(-a, a + 1)))
for i in range(4):
    print(next(gen), end=" ")

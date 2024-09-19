def gen(x):
    from math import pow
    return round(0.5 * pow(x / 100, 2) - 2.0, 2)


count = 0
a, b = map(int, input().split())

res = (gen(i) for i in range(a * 100, b * 100))

print(*(round(next(res), 2) for i in range(20)))

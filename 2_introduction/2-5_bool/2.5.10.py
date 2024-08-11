a, b, c = map(int, input().split())
res = a + b > c and a + c > b and b + c > a
print(res)
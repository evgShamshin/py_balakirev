a, b = input().split()
a = a[1:len(b):2]
b = b[1::2]
print(a == b)
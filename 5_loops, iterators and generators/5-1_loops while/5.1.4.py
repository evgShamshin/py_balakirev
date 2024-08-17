n = float(input())
s = 1.0
count = 2.0

while count < n + 1:
    s += 1 / count
    count += 1

print(round(s, 3))
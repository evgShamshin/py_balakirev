# put your python code here
p = [0] * 10

while p.count(1) < 5:
    p[int(input())] = 1

print(*p)
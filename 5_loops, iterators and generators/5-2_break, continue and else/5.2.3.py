# put your python code here
num = int(input())
res = 1
res *= num if num > 0 else 1

while num != 0:
    num = int(input())
    res *= num if num > 0 else 1

print(res)
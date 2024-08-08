# put your python code here
d_in = input().split()
res = {}
num = int(d_in[0])
res[num] = d_in[1]

for i in range(2, len(d_in)):
    num += 1
    res[num] = d_in[i]

print(res[4])
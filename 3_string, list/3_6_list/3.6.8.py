l_in = []

for i in range(4):
    l_in.append(input())

del(l_in[2])
l_in[1] = "Пушкин"
l_in[2] = float(l_in[2]) * 2

print(l_in)
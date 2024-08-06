d_in = list(input().split())
s = set()
num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

for i_1 in range(len(d_in)):
    for i_2 in range(len(d_in[i_1])):
        if d_in[i_1][i_2].isdigit():
            s.add(int(d_in[i_1][i_2]))
        else:
            s.add(d_in[i_1][i_2])

res = s.intersection(num)
print(*sorted(res)) if len(res) > 0 else print("НЕТ")
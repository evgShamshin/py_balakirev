l = [input().split() for _ in range(5)]
l_l = []
l_r = []
flag = 0

for _1 in range(5):
    if flag != 0:
        break
    for _2 in range(5):
        if l[_1][_2] != l[_2][_1]:
            print("НЕТ")
            flag += 1
            break

else:
    print("ДА")
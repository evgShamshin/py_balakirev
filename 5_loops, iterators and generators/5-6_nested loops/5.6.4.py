l = []
count = 0
for i in range(5):
    l.append(input().split())


for _1 in range(4):
    if count > 0:
        break

    count = 0
    for _2 in range(4):
        if l[_1][_2] == "1":
            if _1 == 0:
                if _2 == 0:
                    if  l[_1][_2 - 1] == "1" or l[_1][_2 + 1] == "1" or l[_1 + 1][_2] == "1" or l[_1 + 1][_2 + 1] == "1":
                        print("НЕТ")
                        count += 1
                        break
                else:
                    if l[_1][_2 - 1] == "1" or l[_1][_2 + 1] == "1" or l[_1 + 1][_2] == "1" or l[_1 + 1][_2 - 1] == "1" or l[_1 + 1][_2 + 1] == "1":
                        print("НЕТ")
                        count += 1
                        break
            else:
                if _2 == 0:
                    if l[_1][_2 - 1] == "1" or l[_1][_2 + 1] == "1" or l[_1 - 1][_2] == "1" or l[_1 + 1][_2] == "1" or l[_1 - 1][_2 + 1] == "1" or l[_1 + 1][_2 + 1] == "1":
                        print("НЕТ")
                        count += 1
                        break
                else:
                    if l[_1][_2 - 1] == "1" or l[_1][_2 + 1] == "1" or l[_1 - 1][_2] == "1" or l[_1 + 1][_2] == "1" or l[_1 - 1][_2 - 1] == "1" or l[_1 - 1][_2 + 1] == "1" or l[_1 + 1][_2 - 1] == "1" or l[_1 + 1][_2 + 1] == "1":
                        print("НЕТ")
                        count += 1
                        break
if count == 0:
    print("ДА")
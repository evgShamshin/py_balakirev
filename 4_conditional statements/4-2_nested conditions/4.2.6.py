year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, num = list(map(int, input().split()))
res = []

def yesterday_and_tomorrow(month, num):
    if 1 < num < year[month - 1]:
        res.append([str(month), str(num - 1)])
        res.append([str(month), str(num + 1)])

    elif num == year[month - 1]:
        res.append([str(month), str(num - 1)])
        res.append([str(month + 1), "01"])

    elif num == 1:
        res.append([str(month - 1), str(year[month - 1])])
        res.append([str(month), str(num + 1)])

    for i in range(len(res)):
        for j in range(len(res[i])):
            if len(res[i][j]) < 2:
                res[i][j] = "0" + str(res[i][j])

    for i in res:
        print(*i, sep = ".", end = " ")

yesterday_and_tomorrow(month, num)
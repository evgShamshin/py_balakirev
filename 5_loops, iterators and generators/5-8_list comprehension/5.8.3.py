def get_line(num):
    temp = []
    res = []

    for i in range(num + 1):
        res.append(temp) if temp != [] else ""
        temp = []
        for j in range(num):
            temp.append(0) if i != j else temp.append(1)

    return res

[print(*i) for i in get_line(int(input()))]
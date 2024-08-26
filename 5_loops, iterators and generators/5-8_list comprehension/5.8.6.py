def get_line(num):
    temp = []
    res = []

    for i in range(num + 1):
        res.append(temp) if temp != [] else ""
        temp = []
        for j in range(num):
            temp.append(i)

    return res

num = int(input())
[print(*i) for i in get_line(num)]
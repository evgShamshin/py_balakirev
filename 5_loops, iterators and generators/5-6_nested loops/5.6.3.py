def simple_num(num):
    l_num = []
    count = 0

    for _1 in range(2, num + 1):
        for _2 in range(2, _1 + 1):
            if _1 % _2 == 0 and _1 != _2:
                count += 1
        l_num.append(_1) if count == 0 else 1
        count = 0

    return l_num

num_in = int(input())
print(*simple_num(num_in)[:-1]) if simple_num(num_in)[-1] == num_in else print(*simple_num(num_in))
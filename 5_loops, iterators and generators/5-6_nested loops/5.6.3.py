num_in = int(input())
res = []

def simple_num(num):
    l_num = []
    count = 0

    for _1 in range(1, num + 1):
        for _2 in range(2, _1 + 1):
            if _1 % _2 == 0 or _1 != _2:
                count += 1
        l_num.append(_1) if count == 0 else 1
        count = 0

    return l_num

#res = [i for i in range(num_in) if i]
print(simple_num(num_in))
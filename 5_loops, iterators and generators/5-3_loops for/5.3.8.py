def simple_num(num):
    res = "ДА"
    if len([i for i in range(2, num) if num % i == 0]) > 0:
        res = "НЕТ"
    return res

print(simple_num(int(input())))
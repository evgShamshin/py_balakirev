_1 = bin(2 ** 1)  # 0b10
_5 = bin(2 ** 5)  # 0b100000
n = int(input())

print('ДА') if (n & 0b10 == 0b10) or (n & 0b100000 == 0b100000) else print("НЕТ")
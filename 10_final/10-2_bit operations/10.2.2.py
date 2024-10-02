n = int(input())  # начальное значение
bit_position = 3  # позиция бита, который нужно включить
bit_on = 2 ** bit_position # формула для вычисления включения бита
if bin(n)[-3] != "0":
    n += bit_on
print(n)
print(type(bin(8)))
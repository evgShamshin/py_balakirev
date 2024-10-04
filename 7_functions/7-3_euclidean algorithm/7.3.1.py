def get_nod(a, b):
    """Медленный алгоритм Евклида.
Вычисляет и вовзращает НОД для натуральных чисел a и b"""


    while a != b:
        if a < b: a, b = b, a
        a %= b

    return a, b


#print(get_nod.__doc__)
print(get_nod(186,4))
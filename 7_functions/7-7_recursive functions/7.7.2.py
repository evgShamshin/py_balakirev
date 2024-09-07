def get_rec_N(N, count = 1):
    if count < N:
        print(count)
        count += 1
        get_rec_N(N, count)


# считывание числа N
N = int(5)
# вызов рекурсивной функции
get_rec_N(N)
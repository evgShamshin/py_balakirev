import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]
count = 0

# здесь продолжайте программу
for row in range(N):
    for pos in range(N):
        if count < 10 and row % 2 == 0 and pos % 2 == 0:
            count += 1
            P[row][pos] = 1

print()
print(*P, sep="\n")

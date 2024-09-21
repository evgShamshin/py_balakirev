def tribonacci(n):
    # Функция проходится циклом от 1 до n. Возвращает сумму трех предыдущих чисел в цикле при учете, что первые три числа равны 1
    a = [1, 1, 1]
    for i in range(n):
        a.append(a[i] + a[i + 1] + a[i + 2])
        yield a[i]


print(*list(tribonacci(int(input()))))

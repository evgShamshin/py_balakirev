def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, int(input()) + 1):
    print(fibonacci(i), end = " ")
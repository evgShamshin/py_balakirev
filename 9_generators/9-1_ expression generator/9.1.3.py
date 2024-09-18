# ввод значений a и b (переменные a и b не менять!)
a, b = map(int, input().split())

# здесь продолжайте программу
tp = tuple(abs(x) for x in range(a, b+1))
print(*tp[:5], sep='\n')
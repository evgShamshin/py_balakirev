import random
import string

random.seed() #установка "зерна" датчика случайных чисел
print(random.random()) #генерация вещественных случайных величин в диапазоне [0; 1)
print(random.randint(1, 10)) #генерация целочисленных случайных величин в диапазоне [a; b]
print(random.gauss(1, 2)) #генерация гауссовских случайных величин
print(random.choice(string.ascii_uppercase)) #выбор случайного элемента из последовательности
print(random.shuffle([1, 2, 3])) #перемешивание элементов последовательности. Возвращает None
print(random.sample(string.ascii_uppercase, 3)) #выбор случайной подпоследовательности из последовательности
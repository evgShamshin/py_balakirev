import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
res = {}
[res.setdefault(i.split("=")[0],i.split("=")[1]) for i in lst_in]
menu.update(res)
[print(i[0], end=" ") for i in menu.items()]
print()
[print(i[1], end=" ") for i in menu.items()]
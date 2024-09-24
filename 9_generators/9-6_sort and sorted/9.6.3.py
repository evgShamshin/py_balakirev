def get_sort(d):
    return [d[i] for i in sorted(d, reverse=True)]

print(get_sort({'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}))
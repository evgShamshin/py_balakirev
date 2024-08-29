t = [
    "– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

lst = []
temp = []

for j in [i.split() for i in t]:
    temp = []
    for k in j:
        temp.append(k) if len(k) > 3 else ""
    lst.append(temp)

print(lst)
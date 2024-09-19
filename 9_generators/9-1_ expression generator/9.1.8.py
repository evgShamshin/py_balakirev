cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
count = 0

gen = ([city for city in cities] for _ in range(1000000))


for city in gen:
    temp = city
    if count + len(temp) <= 20:
        count += len(temp)
        print(*temp, end = " ")
    else:
        print(*temp[:20 - count], end = " ")
        break
towns = input().lower().replace("ь", "").replace("ъ", "").replace("ы", "").split()
res = []

for town in range(1, len(towns)):
    res.append(towns[town]) if towns[town - 1][-1] == towns[town][0] else 0

print("ДА") if len(res) + 1 == len(towns) else print("НЕТ")

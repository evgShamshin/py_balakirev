# put your python code here
res = "ДА"

for town in input().split():
    if len(town) < 5:
        res = "НЕТ"
        break

print(res)
d = {"green": 3.0, "red": 2.0}
num = float(input())
count = 0.0
res = ""

while count < num:
    if float(count + d["green"]) <= num:
        count += d["green"]
    else:
        res = "green"
        break
    if float(count + d["red"]) <= num:
        count += d["red"]
    else:
        res = "red"
        break

print(res)
s = input().lower()
res = [-1]

for i, d in enumerate(s):
    if s[i:i+2] == "ра":
        res.append(i)

print(res[0]) if len(res) == 1 else print(*res[1:])
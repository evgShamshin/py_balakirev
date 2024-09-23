s = "Sergey Balakirev"
lst = []

for i, k in enumerate(s):
    lst.append(tuple([k, i]))

lst = lst[:10] if len(lst) >= 10 else lst
print(lst)
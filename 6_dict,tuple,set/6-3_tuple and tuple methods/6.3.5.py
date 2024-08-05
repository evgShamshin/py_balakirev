l = input().split()
if "Ульяновск" in l:
    l.remove("Ульяновск")
l = tuple(l)
print(l)
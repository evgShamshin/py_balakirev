t_in = tuple([input().split()])
if "Москва" not in t_in[0]:
    t_in[0].append("Москва")
print(*t_in[0])
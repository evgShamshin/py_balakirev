def get_data_fig(*args, tp=False, color=0, closed=False, width=0):
    res = [sum(list(map(int, str(args).rstrip("),'").lstrip("(',").replace(",", "").split())))]
    if tp:
        res.append(tp)
    if color != 0:
        res.append(color)
    if width != 0:
        res.append(closed)
        res.append(width)
    return res


print(*get_data_fig("1 2 3 4 3 2 4"))

def less_six(txt):
    return [i for i in txt.split() if len(i) >= 6]


print(*less_six(input()))
def create_global(x):
    global TOTAL
    TOTAL = x
    return TOTAL


print(create_global(input()))
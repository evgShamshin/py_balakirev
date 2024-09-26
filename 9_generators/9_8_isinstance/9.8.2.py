def get_add(a, b):
    if type(a) in (float, int) and type(b) in (float, int):
        return a + b
    elif type(a) == str and type(b) == str:
        return a + b
    else:
        return None


print(get_add("2", "2.2"))

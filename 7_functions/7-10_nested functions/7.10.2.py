def counter_add(u):
    def hz():
        return u + 2

    return hz


k = int(input())
counter = counter_add(k)
print(counter())

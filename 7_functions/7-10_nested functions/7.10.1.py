def counter_add(u):
    def hz():
        return u + 5

    return hz


k = int(input())
cnt = counter_add(k)
print(cnt())

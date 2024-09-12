def sort_list(func):
    def wrapper(z):
        return sorted(func(z))

    return wrapper


@sort_list
def get_list(l):
    return list(map(int, l.split()))


print(*get_list(input()))

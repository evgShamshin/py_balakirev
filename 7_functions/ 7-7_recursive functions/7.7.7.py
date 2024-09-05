def get_path(n, count=0):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 0:
        count += get_path(n - 1, count) + get_path(n - 2, count)
    return count


print(get_path(int(input())))

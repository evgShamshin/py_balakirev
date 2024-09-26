def get_even_sum(it):
    return sum(filter(lambda x: type(x) == int and x % 2 == 0, it))

print(get_even_sum([3.3]))
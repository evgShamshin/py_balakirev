def get_sum(it):
    return sum(filter(lambda x: type(x) == int, it))

print(get_sum([1,2,3]))
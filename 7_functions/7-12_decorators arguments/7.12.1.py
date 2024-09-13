def sum_of_num_plus5(start=5):
    def decorator(func):
        def wrapper(l):
            wrapper.__name__ = func.__name__
            return func(l) + start

        return wrapper

    return decorator


@sum_of_num_plus5(start=5)
def sum_of_num(l):
    return sum(map(int, l.split()))


print(sum_of_num(input()))
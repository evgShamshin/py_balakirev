def sum_to_num(num):
    def decorator(func):
        def wrapper(*args):
            wrapper.__doc__ = func.__doc__
            wrapper.__name__ = func.__name__
            return num + sum(func(*args))

        return wrapper

    return decorator


@sum_to_num(0)
def get_list(n):
    '''Функция для формирования списка целых значений'''
    return list(map(int, n.split()))

print(get_list(input()))
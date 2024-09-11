def func_show(func):
    def wrapper(*args, **kwargs):
        print(f"Площадь прямоугольника: {args[0] * args[1], kwargs}")

    return wrapper


@func_show
def get_sq(width, height):
    return width, height


get_sq(8, 11)
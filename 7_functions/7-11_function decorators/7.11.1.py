def func_show(func):
    def wrapper(width, height):
        func(width, height)
        #       width, height = map(int, input().split())
        print(f"Площадь прямоугольника: {width * height}")

    return wrapper


def get_sq(width, height):
    return (width, height)

def get_menu(func):
    def wrapper(*args):
        _list = [[pos + 1, i] for pos, i in enumerate(args[0].split())]
        for i in _list:
            print(f"{i[0]}. {i[1]}")

    return wrapper


@get_menu
def show_menu(*l):
    return l


menu = input()
show_menu(menu)

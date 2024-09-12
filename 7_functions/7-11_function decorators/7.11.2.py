def get_menu(func):
    def wrapper(l):
        for pos, i in enumerate(func(l)):
            print(f"{pos + 1}. {i}")


    return wrapper


@get_menu
def show_menu(l):
    return l.split()


menu = input()
show_menu(menu)
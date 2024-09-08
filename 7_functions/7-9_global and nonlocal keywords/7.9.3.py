WIDTH = int(input())


def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())
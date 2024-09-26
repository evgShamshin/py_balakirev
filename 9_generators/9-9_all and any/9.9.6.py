import sys

def is_free(lst):
    return any(map(lambda x: any(i=="#" for i in x), lst))


lst_in = list(map(str.strip, sys.stdin.readlines()))
pole = list(map(str.split, lst_in))
print(is_free(pole))
def get_list_dig(lst):
    return [i for i in lst if type(i) in (int, float)]

print(get_list_dig([1, 2, 3, "4"]))
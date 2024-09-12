def get_dict(func):
    def wrapper(_list):
        res = {}
        for _1 in range(len(_list) - 1):
            for _2 in range(len(_list[_1])):
                res[_list[_1][_2]] = _list[_1 + 1][_2]
        return res

    return wrapper


@get_dict
def get_tuple(l):
    return l


d_in = [input().split() for _ in range(2)]
print(*sorted(get_tuple(d_in).items()))
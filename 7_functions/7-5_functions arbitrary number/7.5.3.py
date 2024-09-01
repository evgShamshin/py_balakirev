def get_biggest_city(*args):
    res = sorted(args, key=len)
    return res[-1]
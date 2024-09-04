def get_rec_sum(l, l_len=0, l_sum=0):
    if type(l) == str:
        l = list(map(int, l.split()))
    if l_len < len(l):
        l_sum += l[l_len]
        get_rec_sum(l, l_len + 1, l_sum)
    elif l_len == len(l):
        print(l_sum)


get_rec_sum(input())
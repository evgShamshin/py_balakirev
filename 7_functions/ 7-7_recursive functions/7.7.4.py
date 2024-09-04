def fib_rec(N, f_num=[1, 1], f_len=2):
    if N > f_len:
        temp = f_num[f_len - 2] + f_num[f_len - 1]
        f_num.append(temp)
        f_len += 1
        fib_rec(N, f_num, f_len)
    return f_num


print(fib_rec(7))
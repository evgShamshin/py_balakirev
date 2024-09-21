s = input()
s_lst = s.split()

tp = tuple(tuple(i.split("=")) for i in s_lst)
tp = tuple(map(lambda x: tuple(x.split("=")), s_lst))

print(tp)
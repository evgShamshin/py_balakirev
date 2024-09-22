l_num_in = map(int, input().split())
l_num_out = filter(lambda x: len(str(abs(x))) == 2, l_num_in)
print(*l_num_out, sep=' ')
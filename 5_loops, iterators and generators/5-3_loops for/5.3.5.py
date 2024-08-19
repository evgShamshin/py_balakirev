l_num = list(map(int, input().split()))
print(sum([i for i in l_num if i % 2 != 0]))
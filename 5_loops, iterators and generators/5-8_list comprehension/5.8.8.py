lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

[print(lst_1[i] + lst_2[i], end=' ') for i in range(len(lst_1))]
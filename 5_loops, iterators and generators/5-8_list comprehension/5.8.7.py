fl_l = list(map(float, input().split()))
[print(fl_l[i], end=' ') for i in range(len(fl_l)) if i % 2 == 0]
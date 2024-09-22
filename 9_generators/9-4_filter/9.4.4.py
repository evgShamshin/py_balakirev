num_in_1, num_in_2 = ((set(map(int, input().split()))) for i in range(2))
num_out = num_in_1.intersection(num_in_2)
[print(num, end=" ") for num in sorted(filter(lambda x: x % 2 == 0, num_out))]
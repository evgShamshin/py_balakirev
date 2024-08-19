num_in = int(input())
print(*[num for num in range(1, num_in + 1) if num_in % num == 0], sep="\n")
def matrix_step(l):
    max_i = 0
    for i in range(len(l)):
        if i * i <= len(l): max_i = i
    return max_i


towns = input().split()
step = matrix_step(towns)
count = 0
len_towns = len(towns) - len(towns) % step

for i in range(len_towns):
    count += 1
    if count < step:
        print(towns[i], end=" ")
    else:
        print(towns[i], end="\n")
        count = 0
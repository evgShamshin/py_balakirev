import time
def sort_my(l):
    "Сортировка пузырьком"
    start_time = time.time()
    while l != sorted(l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]

    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


l = list(map(int, input().split(",")))
print(sort_my(l))
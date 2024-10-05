import time

def sort_my(l):
    "Сортировка БЕЗ пузырька :)"
    start_time = time.time()
    while l != sorted(l):
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

l = list(map(int, input().split(",")))
print(sort_my(l))
def sort_my(l):
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
    return l


l = list(map(int, input().split()))
print(*sort_my(l), sep=" ")
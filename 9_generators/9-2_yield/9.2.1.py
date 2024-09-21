N = int(input())

def get_sum(N):
    for i in range(1, N + 1):
        yield sum(range(1, i + 1))


a = get_sum(N)
print(*list(a))
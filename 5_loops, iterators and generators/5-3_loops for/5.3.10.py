n = int(input())
print(sum([i for i in range(1, n) if i % 3 == 0 or i % 5 == 0]))
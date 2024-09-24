l_1, l_2 = sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())), reverse=True)
print(*[i + k for i, k in (zip(l_1, l_2))])
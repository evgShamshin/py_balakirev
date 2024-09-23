l_in_1, l_in_2 = (map(int, input().split()) for _ in range(2))

l_out = tuple(i * j for i, j in zip(l_in_1, l_in_2))
print(*l_out[:3])
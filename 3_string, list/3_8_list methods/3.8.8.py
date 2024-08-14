lst = list(map(int, input().split()))
lst.append(True) if lst[-1] % 2 != 0 else lst.append(False)
lst.pop(-2)
print(*lst)
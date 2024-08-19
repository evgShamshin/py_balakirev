lst = input().split()
lst.append(False) if lst[-1] == lst[0] else lst.append(True)
print(*lst)
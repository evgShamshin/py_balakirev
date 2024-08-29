def min_max_sum(l):
    return (f"Min = {min(l)}, max = {max(l)}, sum = {sum(l)}")

l_in = list(map(int, input().split()))
print(min_max_sum(l_in))
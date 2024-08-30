def get_not_even(n):
    return n % 2 != 0


lst_d = list(map(int, input().split()))
print(*[i for i in lst_d if get_not_even(i)])
set_1 = set(input().split())
set_2 = set(input().split())

print("ДА") if set_1 >= set_2 or set_2 >= set_1 else print("НЕТ")
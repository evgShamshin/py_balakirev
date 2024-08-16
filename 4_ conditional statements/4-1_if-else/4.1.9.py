num = list(input())
print(("НЕТ", "ДА")[sum(list(map(int, list((num[:3]))))) == sum(list(map(int, list(map(int, (num[-1:-4:-1]))))))])
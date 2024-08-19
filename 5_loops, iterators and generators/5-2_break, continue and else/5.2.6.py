num = int(input())
if num < 100:
    res = [i for i in range(1, num + 1) if i % 3 == 0 and i % 5 == 0]
    print(*res, sep=" ")
else:
    print("слишком большое значение n")
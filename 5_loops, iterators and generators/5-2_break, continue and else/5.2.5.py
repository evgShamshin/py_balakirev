# put your python code here
names = input().lower().split()

res = any([name[0] == name[-1] for name in names])

print("ДА") if res == True else print("НЕТ")
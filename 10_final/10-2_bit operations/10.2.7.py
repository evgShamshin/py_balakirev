s = input()
key = 123
res = [chr(ord(x) ^ key) for x in s]
print(*res, sep="")
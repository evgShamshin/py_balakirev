s = list(input().split("-"))

while "" in s:
    s.remove("")

print(*s, sep = "-")
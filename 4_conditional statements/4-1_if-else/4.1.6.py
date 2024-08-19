l = set(input().lower())
print(("НЕТ", "ДА")[{"t", "h", "o"}.intersection(l) == {"t", "h", "o"}])
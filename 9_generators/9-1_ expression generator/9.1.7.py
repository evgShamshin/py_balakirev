from string import ascii_lowercase

gen = ((i, y) for i in ascii_lowercase for y in ascii_lowercase)
[print(*next(gen), sep = "", end = " ") for _ in range(50)]
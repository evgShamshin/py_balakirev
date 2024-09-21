import random
from string import ascii_lowercase, ascii_uppercase


random.seed(1)


def get_password(N):
    chars = ascii_lowercase + ascii_uppercase
    for i in range(N):
        yield "".join(chars[random.randint(0, len(chars) - 1)])


N = int(input())
for i in range(5):
    for j in get_password(N):
        print(j, end="")
    print("@mail.ru")
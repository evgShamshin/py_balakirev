import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)


def get_password(N):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    for i in range(N):
        yield chars[random.randint(0, len(chars) - 1)]


N = int(input())
[print(*list(get_password(N)), sep="") for _ in range(5)]
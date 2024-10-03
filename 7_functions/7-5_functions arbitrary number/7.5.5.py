import sys


def verify(l):
    flag = False
    for i in range(len(l) - 1):
        if len(l) == 2 and sum(l[i]) >= 1: return flag
        for j in range(len(l) - 1):
            print(f"i, j, {i},{j}")
            if (l[i][j] + l[i][j + 1] + l[i + 1][j] + l[i + 1][j + 1]) > 1:
                return flag
        else:
            continue
        break
    else:
        flag = True

    return flag


lines = sys.stdin.readlines()
lst2D = [list(map(int, i.rstrip().split())) for i in lines]
print(verify(lst2D))

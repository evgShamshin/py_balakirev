t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case num, author, book:
        print("Yes")
    case num, author, book, cost:
        print("Yes")
    case num, author, book, year:
        print("Yes")
    case num, author, book, cost, year:
        print("Yes")
    case _:
        print("No")
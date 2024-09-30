t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case num, author, book if len(author) > 5 and len(book) > 9:
        print("Yes")
    case num, author, book, cost if len(author) > 5 and cost > 0:
        print("Yes")
    case num, author, book, year if year > 2019:
        print("Yes")
    case num, author, book, cost, year if cost > 0 and year > 2019:
        print("Yes")
    case _:
        print("No")
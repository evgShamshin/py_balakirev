def check_email(m):
    flag = False
    t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
         'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y',
         'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@',
         '.'}
    if m.count("@") > 1 or m.count(".") == 0 or m.count("@") == 0:
        return flag
    domen = m.split("@")

    try:
        domen_1, domen_2 = domen[1].split(".")
    except ValueError:
        return flag

    if any([domen_2 == "com", domen_2 == "ru"]) == True and {i for i in domen_1}.issubset(t) and set(domen[0]).issubset(
            t):
        flag = True

    return True if flag else flag


email_in = input().split()
email_out = [email for email in email_in if check_email(email) == True]
print(*email_out)
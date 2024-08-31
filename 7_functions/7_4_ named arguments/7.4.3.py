def check_password(key, chars = "$%!?@#"):
    return all([len(key) >= 8, len([i for i in key if i in chars]) >= 1])


print(check_password('12345678!'))
def rus_to_eng(func):
    def wrapper(l):
        temp = []
        for i in range(len(func(l))):
            for j in range(len(func(l)[i])):
                if func(l)[i][j] in t:
                    temp.append(t[func(l)[i][j]])
                else:
                    temp.append(func(l)[i][j])
            print(*temp, sep="", end="-")\
                if i < len(func(l)) - 1\
                else print(*temp, sep="")
            temp = []


    return wrapper


@rus_to_eng
def get_word(s):
    return s.lower().replace("-", "").split()


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

s = input()
get_word(s)
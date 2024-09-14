t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def txt_chars(*chars):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.__name__ = func.__name__
            data_wrapper = func(*args, c=" ")
            for i in chars[0].split(): data_wrapper = data_wrapper.replace(i, "-")
            return data_wrapper

        return wrapper

    return decorator


@txt_chars("! --- -- -")
def txt_rus_to_eng(txt, **kwargs):
    return ''.join(t.get(c, c) if c not in kwargs.values() else "-" for c in txt.lower())


print(txt_rus_to_eng(input()))
def txt_with_tag(tag="h1"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.__name__ = func.__name__
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper

    return decorator


@txt_with_tag(tag="div")
def txt_to_lower(s):
    return s.lower()


print(txt_to_lower(input()))
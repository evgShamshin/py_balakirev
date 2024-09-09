def txt_to_path(txt):
    def get_path():
        return f"<h1>{txt}</h1>"

    return get_path


s = txt_to_path(input())
print(s())
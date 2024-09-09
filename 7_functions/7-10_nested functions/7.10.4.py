def txt_to_path(txt, tag="h1"):
    def get_path():
        return f"<{tag}>{txt}</{tag}>"

    return get_path


tag = input()
txt = input()

s = txt_to_path(txt, tag=tag)
print(s())
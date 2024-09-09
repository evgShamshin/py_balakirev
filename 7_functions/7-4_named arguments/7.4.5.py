def add_tag(txt, tag="h1"):
    return f"<{tag}>{txt}</{tag}>"

s = input()
print(add_tag(s))
print(add_tag(s, tag="div"))
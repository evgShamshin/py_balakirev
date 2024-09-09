def add_tag(txt, tag="h1", up=True):
    return f"<{tag.upper()}>{txt}</{tag.upper()}>" if up else f"<{tag.lower()}>{txt}</{tag.lower()}>"

s = input()
print(add_tag(s, tag="div"))
print(add_tag(s, tag="div", up=False))
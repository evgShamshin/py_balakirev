def convert_to(txt, tp):
    def to():
        return list(map(int, txt.split())) if tp == "list" else tuple(map(int, txt.split()))

    return to


tp = input()
txt = input()
res = convert_to(txt, tp)
print(res())
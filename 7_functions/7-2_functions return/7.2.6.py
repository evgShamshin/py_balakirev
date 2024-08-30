tp = input().strip()

if tp == "RECT":
    def get_sq(length, widht):
        return length * widht
else:
    def get_sq(length):
        return length ** 2
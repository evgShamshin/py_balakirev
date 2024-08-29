def p_p(width, height):
    return(width * 2 + height * 2)

w, h = list(map(int, input().split()))
print(f"Периметр прямоугольника, равен {p_p(w, h)}")
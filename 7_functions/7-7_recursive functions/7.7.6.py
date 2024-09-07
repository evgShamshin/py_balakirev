d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

# здесь продолжайте программу
def get_line_list(l, l_line=[]):
    for i in l:
        if type(i) == list:
            get_line_list(i, l_line)
        else:
            l_line.append(i)
    return l_line
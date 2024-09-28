student = ['Троечников С.М.', 2, 3, 3, 2, 3, 4, 3, 5, 5, 1]

match student:
    case fio, m1, m2, m3:               # 1-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case tuple() as fio, m1, m2, m3, *_: # 2-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case list() as fio, m1, m2, m3, *_: # 3-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case tuple() as fio, m1, m2, m3:    # 4-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case _:                             # 5-й case
        print("Некорректный формат данных")
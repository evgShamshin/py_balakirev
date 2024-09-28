sel_id = 2

match sel_id:
    case 1:
        print("Выбран пункт номер "+str(sel_id))
    case 5:
        print("Выбран пункт номер "+str(sel_id))
    case _:
        print("Неверный пункт меню")
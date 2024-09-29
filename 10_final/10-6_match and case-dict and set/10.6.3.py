json_data = {'fio': 'sm_b', 'marks': [2, 2, 3, 2, 3, 4], 'age': 22}

match json_data:
    case {'marks': ms, 'age': age, 'fio': fio} if ms.count(2) > 1:
        print(ms)
    case {'marks': ms, 'age': int() | float() as age, 'fio': fio} if ms.count(2) > 1:
        print(ms)
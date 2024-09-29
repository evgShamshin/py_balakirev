json_data = {'fio': 'sm_b', 'marks': [2, 2, 3, 2, 3, 4], 'age': 22}

match json_data:
#    case {'fio': f, 'marks': ms, 'age': ag}:
#        print(f, ms, ag)
#    case {'marks': m, 'age': 22}:
#        print(m)
    case {'marks': ms, 'age': age, 'fio': fio} if age == 22:
        print(fio)
    case {'marks': ms, 'age': age} if age == 22:
        print(ms)
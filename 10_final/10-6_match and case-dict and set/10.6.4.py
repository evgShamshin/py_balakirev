def parse_json(data):
    match data:
        case {'access': bool() as access, 'data': list() as date}:
            return (access, date[0])
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login
        case _:  # wildcard
            return None


json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

print(parse_json(json_data))

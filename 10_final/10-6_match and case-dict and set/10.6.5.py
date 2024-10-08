def parse_json(data):
    match data:
        case {'access': True, 'data': [_, {'login': str() as login, 'email': str() as email}, _, *_]}:
            return (login, email)
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login
        case _:  # wildcard
            return None


json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
print(parse_json(json_data))

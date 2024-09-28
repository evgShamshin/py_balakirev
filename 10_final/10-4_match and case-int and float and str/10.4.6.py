def get_data(value):
    match value:
        case int() | float () | str() as value:
            return value

print(get_data(1))
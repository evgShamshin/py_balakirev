def get_data(value):
    match value:
        case int() as value if value > 0:
            return value
        case float() as value if -101 < value < 101:
            return value
        case str() as value:
            return value

print(get_data(1))
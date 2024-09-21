def towns(town, _len=5):
    return town if len(town) > _len else "-"


print(*[towns(town) for town in input().split()])
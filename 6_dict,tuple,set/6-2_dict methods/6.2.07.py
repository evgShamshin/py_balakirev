n = int(input())
t = 0
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

for thing in things:
    things[thing] = things.setdefault(thing, "") / 1000

for thing in sorted(things.items(), key = lambda x: x[1], reverse = True):
    if t + thing[1] <= n:
        t += thing[1]
        print(thing[0], end = " ")
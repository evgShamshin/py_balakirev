distance_in = 10
distance_out = int(input())

day_out = 1

while True:
    if distance_in > distance_out:
        break
    elif distance_in == distance_out or distance_in < distance_out:
        day_out += 1
        distance_in *= 1.1

print(day_out)
'''
s = set()

while True:
    d_in = input()
    if d_in != "q":
        s.add(d_in)
    else:
        break

print(len(s))
'''

lst_in = iter(input, 'q')

print(len(set(lst_in)))
m = ['#до', 'ре', 'ми', '#фа', 'соль', 'ля', 'си']
l = list(map(int, input().split()))
print(f"{m[l[0] - 1]} {m[l[1] - 1]} {m[l[2] - 1]}")
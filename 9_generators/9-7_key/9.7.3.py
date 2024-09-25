correct = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
print(*sorted(input().split(), key=lambda x: correct.index(x)))
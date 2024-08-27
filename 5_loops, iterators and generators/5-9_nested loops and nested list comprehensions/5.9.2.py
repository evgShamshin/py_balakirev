matrix = list(map(int, input().split()))

n = [i
     for i in range(2, len(matrix))
     if len(matrix) // i == i][0]

res = [matrix[i:i+n]
       for i in range(0, len(matrix), n)]

print(res)
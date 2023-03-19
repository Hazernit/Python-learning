n = int(input())

matrix = []
for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

# print(matrix)
total_min = float("inf")
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = matrix[i][j] + matrix[j][k] + matrix[k][i]
            if total_min > total:
                total_min = total
print(total_min)

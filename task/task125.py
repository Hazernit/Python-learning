n = int(input())

matrix = []
for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

# print(matrix)
b = input()

color = list(map(int, input().split()))

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] > 0 and color[i] != color[j]:
            count += 1
count //= 2
print(count)







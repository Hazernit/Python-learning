from collections import deque

# False - black, True - white
# Если сумма координат чётная, то клетка чёрная
def is_black(i, j):
    return (i + j) % 2 == 1


word_in_digit = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
n = 9
graph = [[-1] * n for _ in range(n)]  # Создаём матрицу

start, end = input().split()
x1, y1 = word_in_digit[start[0]], int(start[1]) - 1
x2, y2 = word_in_digit[end[0]], int(end[1]) - 1
# print(x1, y1)

def func(i, j):
    i += 1
    j += 1
    return 1 <= i <= n and 1 <= j <= n


def bfs(i, j):
    queue = deque([(i, j)])
    # print(queue)
    graph[i][j] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()  # Получаем вершину
        if is_black(i, j):
            for x, y in [(i+1, j+2), (i+1, j-2), (i-1, j-2), (i-1, j+2), (i+2, j+1), (i+2, j-1), (i-2, j-1), (i-2, j+1)]:
                if func(x, y) and graph[x][y] == -1:
                    graph[x][y] = graph[i][j]+1
                    queue.append((x, y))
        else:
            for x in range(9):
                for y in range(9):
                    if abs(y-i) == abs(x-j):
                        if graph[y][x] == -1:
                            graph[y][x] = graph[i][j] + 1
                            queue.append((y, x))


bfs(y1, x1)

# for line in graph:
#     print(line)
# print(x2, y2)
print(graph[y2][x2])

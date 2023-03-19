from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]  # Создаём матрицу
# for line in graph:
#     print(line)
graph_distance = [[-1] * n for _ in range(n)]
graph_draw = [[-1] * n for _ in range(n)]

start = (-1, -1)
finish = (-1, -1)
is_start = True
for i in range(len(graph)):
    for j in range(len(graph[i])):
        # print(graph[i][j])
        graph_draw[i][j] = '.'
        if is_start and graph[i][j] == '@':
            start = (i, j)
            graph_draw[i][j] = '@'
            is_start = False
        elif not is_start and graph[i][j] == '@':
            finish = (i, j)
            graph_draw[i][j] = '!'
        if graph[i][j] == '#':
            graph_draw[i][j] = '#'
            graph_distance[i][j] = -2



def func(i, j):
    i += 1
    j += 1
    return 1 <= i <= n and 1 <= j <= n


def bfs_distance(i, j):
    queue = deque([(i, j)])
    # print(queue)
    graph_distance[i][j] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()  # Получаем вершину
        for x, y in [(i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2),
                     (i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1)]:
            if func(x, y) and graph_distance[x][y] == -1:
                graph_distance[x][y] = graph_distance[i][j] + 1
                queue.append((x, y))


bfs_distance(start[0], start[1])

# if graph2_draw[finish[0]][finish[1]] != '@':
#     print("Impossible")
# else:

is_passed = True
if graph_distance[finish[0]][finish[1]] == -1:
    is_passed = False

if is_passed:
    st = graph_distance[finish[0]][finish[1]]
    i = finish[0]
    j = finish[1]
    graph_draw[i][j] = "@"
    while st > 1:
        for x, y in [(i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2),
                     (i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1)]:
            if func(x, y) and st == graph_distance[x][y]+1:
                graph_draw[x][y] = "@"
                i = x
                j = y
                st -= 1

# for line in graph_distance:
#     print(*line, sep="")
# print()

if is_passed:
    for line in graph_draw:
        print(*line, sep="")
else:
    print("Impossible")















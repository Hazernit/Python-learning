from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]  # Создаём матрицу
# print(graph)
graph2_distance = [[-1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == "O":
            graph2_distance[i][j] = -2
        else:
            graph2_distance[i][j] = -1


# Потом меняю тип
start = -1
finish = -1
for i in range(len(graph)):
    for j in range(len(graph[i])):
        # print(graph[i][j])
        if graph[i][j] == '@':
            start = (i, j)
        if graph[i][j] == 'X':
            finish = (i, j)

# print(start)
# print(finish)
def func(i, j):
    i += 1
    j += 1
    return 1 <= i <= n and 1 <= j <= n


def bfs_distance(i, j):
    queue = deque([(i, j)])
    # print(queue)
    graph2_distance[i][j] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()  # Получаем вершину
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if func(x, y) and graph2_distance[x][y] == -1:
                graph2_distance[x][y] = graph2_distance[i][j]+1
                queue.append((x, y))


bfs_distance(start[0], start[1])
# for line in graph2_distance:
#     print(line)
is_passed = False
if graph2_distance[finish[0]][finish[1]] == -1:
    is_passed = False
else:
    is_passed = True

if is_passed:
    st = graph2_distance[finish[0]][finish[1]]
    i = finish[0]
    j = finish[1]
    graph[i][j] = "+"
    while st > 1:
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if func(x, y) and st == graph2_distance[x][y]+1:
                graph[x][y] = "+"
                i = x
                j = y
                st -= 1


if is_passed:
    print("Yes")
    for line in graph:
        print(*line, sep="")
else:
    print("No")


# # Для построения графа
# is_passed = False
# def bfs(i, j):
#     global is_passed
#     queue = deque([(i, j)])
#     # print(queue)
#     # graph[i][j] = '+'
#     # Если длина очереди будет 0, то дальше не пойдём
#     while queue:
#         i, j = queue.popleft()  # Получаем вершину
#         for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
#             if func(x, y) and graph[x][y] == '.':
#                 graph[x][y] = '+'
#                 queue.append((x, y))
#             if func(x, y) and graph[x][y] == 'X':
#                 is_passed = True
#                 graph[x][y] = '+'


# bfs(start[0], start[1])












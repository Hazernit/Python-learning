from collections import deque

n = int(input())

x1, y1 = map(int, input().split())
x1 -= 1
y1 -= 1
x2, y2 = map(int, input().split())
x2 -= 1
y2 -= 1

graph = [[-1] * n for _ in range(n)]  # Создаём матрицу
# print(graph)


def func(i, j):
    i += 1
    j += 1
    return 1 <= i <= n and 1 <= j <= n


def bfs(i, j):
    queue = deque([(i, j)])
    graph[i][j] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()  # Получаем вершину
        for x, y in [(i+1, j+2), (i+1, j-2), (i-1, j-2), (i-1, j+2), (i+2, j+1), (i+2, j-1), (i-2, j-1), (i-2, j+1)]:
            if func(x, y) and graph[x][y] == -1:
                graph[x][y] = graph[i][j]+1
                queue.append((x, y))


bfs(x1, y1)
print(graph[x2][y2])
# used = [False] * n
#
#
# count = 0
# def bfs(start):
#     global count
#     queue = deque([start])
#     used[start] = True
#
#     # Если длина очереди будет 0, то дальше не пойдём
#     while queue:
#         source = queue.popleft()  # Получаем вершину
#         for destination in range(n):
#             if graph[source][destination] == 1 and not used[destination]:
#                 used[destination] = True
#                 count += 1
#                 queue.append(destination)
#
#
# bfs(start-1)
# print(count)
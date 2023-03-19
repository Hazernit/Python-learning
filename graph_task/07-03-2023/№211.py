from collections import deque

w, h = map(int, input().split())
graph = [list(input()) for _ in range(h)]
w += 2
h += 2


def default_graf_distance():
    graph_distance = [[-1] * w for _ in range(h)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != ".":
                graph_distance[i + 1][j + 1] = -2
    return graph_distance


graph_distance = default_graf_distance()
# for line in graph_distance:
#     print(line)

def func(i, j):
    i += 1
    j += 1
    return 1 <= i <= h and 1 <= j <= w

def bfs_distance(i, j):
    queue = deque([(i, j)])
    # print(queue)
    graph_distance[i][j] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()  # Получаем вершину
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if func(x, y) and graph_distance[x][y] == -1:
                graph_distance[x][y] = graph_distance[i][j] + 1
                queue.append((x, y))



while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 == x2 == y2 == 0:
        break
    graph_distance = default_graf_distance()
    graph_distance[y2][x2] = -1
    bfs_distance(y1, x1)
    # for line in graph_distance:
    #     print(line)

    if graph_distance[y2][x2] == -1:
        print(0)
    else:
        print(graph_distance[y2][x2])




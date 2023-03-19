from collections import deque

n, m = map(int, input().split())

start_x, start_y = map(int, input().split())
start_x -= 1
start_y -= 1

graph = [input().split() for _ in range(n)]


graph_distance = [[-1] * m for _ in range(n)]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == '1':
            graph_distance[i][j] = -2


# Туннели
c_hypertunnels = int(input())
hypertunnels_dict = {}
for _ in range(c_hypertunnels):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    hypertunnels_dict[(x1, y1)] = (x2, y2)


# Выход
exits = []
c_exits = int(input())
for _ in range(c_exits):
    x1, y1 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    exits.append((x1, y1))

# for line in graph_distance:
#     print(line)


def func(i, j):
    return 1 <= i + 1 <= n and 1 <= j + 1 <= m

def bfs_distance(i, j):
    queue = deque([(i, j)])
    # print(queue)
    graph_distance[i][j] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()
        find_in_dict = (i, j)
        if find_in_dict in hypertunnels_dict:
            x_h, y_h = hypertunnels_dict[find_in_dict]
            # print("Сработал телепорт из find_in_dict:", find_in_dict, "в x_h:", x_h, "y_h", y_h)
            if graph_distance[x_h][y_h] == -1:
                graph_distance[x_h][y_h] = graph_distance[i][j] + 1
                queue.append((x_h, y_h))
        # Получаем вершину
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if func(x, y) and graph_distance[x][y] == -1:
                graph_distance[x][y] = graph_distance[i][j] + 1
                queue.append((x, y))





bfs_distance(start_x, start_y)
# for line in graph_distance:
#     print(line)

is_escape = False
min_distance = 99999999999
for x, y in exits:
    if graph_distance[x][y] != -1:
        # is_escape = True
        if min_distance > graph_distance[x][y]:
            min_distance = graph_distance[x][y]
        is_escape = True
if is_escape:
    print(min_distance+1)
else:
    print("Impossible")



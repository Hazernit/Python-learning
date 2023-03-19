from collections import deque

n = int(input())
area_of_one_wall_tile = 5 * 5

start_x, start_y = 1, 1
start_x -= 1
start_y -= 1

graph = [list(input()) for _ in range(n)]
for line in graph:
    print(line)

graph_distance = [[-1] * (n + 2) for _ in range(n + 2)]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == '.':
            graph_distance[i + 1][j + 1] = 0
# Несуществующий нижний правый угол
graph_distance[-1][-1] = -3
graph_distance[-1][-2] = -3
graph_distance[-2][-1] = -3
# Несуществующий верхний левый угол
graph_distance[0][0] = -3
graph_distance[0][1] = -3
graph_distance[1][0] = -3
for line in graph_distance:
    print(line)



def func(i, j):
    return 1 <= i + 1 <= n and 1 <= j + 1 <= n


def bfs_distance(i, j):
    painting_area = 0
    queue = deque([(i, j)])
    # print(queue)
    graph_distance[i][j] = -2
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()
        # Получаем вершину
        for x, y in [(i + 1, j), (i - 1, j),
                     (i, j + 1), (i, j - 1)]:
            if func(x, y) and graph_distance[x][y] == 0:
                print(x, y)
                graph_distance[x][y] = -2
                queue.append((x, y))
            if graph_distance[x][y] == -1:
                painting_area += area_of_one_wall_tile
    return painting_area


result = bfs_distance(start_x, start_y)
# for line in graph_distance:
#     print(line)
print(result)


# Запускаем бфс от каждой непосещенной клетки по очереди.
# В бфсе посещенные вершины помечаем.
# В бфсе не заходим за границы поля и на защищенные клетки.
# Сколько раз запустится бфс, столько и отдельных областей на поле.
from collections import deque

n, m = map(int, input().split())
graph = [[False] * m for _ in range(n)]  # Создаём словарь, с ключами от 0 до n-1, а по ключу будут лежать пустые множества

# print(graph)
protected, *coords = map(int, input().split())
# print(coords)
# Добавляем защищенные клетки, чтоб по ним не идти
for i in range(1, len(coords), 2):
    v1, v2 = coords[i-1], coords[i]
    # print(v1, v2)
    graph[v1-1][v2-1] = True
# print(graph)

def func(i, j):
    i += 1
    j += 1
    return 1 <= i <= n and 1 <= j <= m


# Расчитываем расстояние
def bfs(i, j):
    queue = deque([(i, j)])
    graph[i][j] = True
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        i, j = queue.popleft()  # Получаем вершину
        for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
            if func(x, y) and not graph[x][y]:
                graph[x][y] = True
                queue.append((x, y))


count = 0
for i in range(n):
    for j in range(m):
        # print(f"i={i}, j={j}")
        if not graph[i][j]:
            bfs(i, j)
            count += 1
print(count)


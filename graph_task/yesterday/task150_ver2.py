from collections import deque

n, start = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]  # Создаём матрицу
# graph

used = [False] * n


count = 0
def bfs(start):
    global count
    queue = deque([start])
    used[start] = True

    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        source = queue.popleft()  # Получаем вершину
        for destination in range(n):
            if graph[source][destination] == 1 and not used[destination]:
                used[destination] = True
                count += 1
                queue.append(destination)


bfs(start-1)
print(count)


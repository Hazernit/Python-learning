from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]  # Создаём матрицу
# graph
start, end = map(int, input().split())
start -= 1
end -= 1


distances = [-1] * n
def bfs(start):
    used = [False] * n

    queue = deque([start])
    used[start] = True
    distances[start] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        source = queue.popleft()  # Получаем вершину
        for destination in range(n):
            if graph[source][destination] == 1 and not used[destination]:
                used[destination] = True
                queue.append(destination)

                distances[destination] = distances[source]+1
    # return distances


bfs(start)

answer = distances[end]
print(answer)




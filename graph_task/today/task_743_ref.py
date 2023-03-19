from collections import deque

graph = {}

# used = [False] * n_vertex
# used = {}
distances = {}

n = int(input())
for _ in range(n):
    a, b = input().split(" -> ")
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = []
    # used[a] = False
    distances[a] = -1
    distances[b] = -1


start = input()
finish = input()

visited = []   # List for visited nodes.
queue = []  # Initialize a queue
# n_vertex = len(graph.keys())

# Мы добавляем в

def bfs(start):
    queue = deque([start])
    # used[start] = True
    distances[start] = 0
    # Если длина очереди будет 0, то дальше не пойдём
    while queue:
        source = queue.popleft()  # Получаем вершину
        for destination in graph[source]:
            if distances[destination] == -1:
                queue.append(destination)
                distances[destination] = distances[source] + 1
    # return distances
if start in graph:
    bfs(start)
else:
    answer = -1

# print(distances)
if finish in distances:
    answer = distances[finish]
elif start == finish:
    answer = 0
else:
    answer = -1
print(answer)


from collections import deque

graph = {}

# used = [False] * n_vertex
# used = {}
distances = {}

n = int(input())
for i in range(n):
    line = list(input().split())
    for j in range(len(line)):
        # print(line)
        if line[j] == "1":
            if i+1 not in graph:
                graph[i+1] = [j+1]
            else:
                graph[i+1].append(j+1)
            distances[i+1] = -1
            distances[j+1] = -1

{"1": ["2"], "2": ["1", "3"], "3": ["2"]}
print(graph)


visited = []   # List for visited nodes.
queue = []  # Initialize a queue
# n_vertex = len(graph.keys())

# Мы добавляем в
answer = [True]
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






















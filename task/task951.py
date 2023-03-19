import collections  # для удаления сначала и добавления в конец

#graph - матрица
#root или node - первая вершина
#queue - очередь

visited = []
queue = []

def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

data = list(map(int, input().split()))
n = data[0]
data.pop(0)

for i in range(len(data)):

while data:
    i = data[0]
    j = data[1]
    t = 0
    info = (i, j, t)
    data.pop(0)
    data.pop(1)




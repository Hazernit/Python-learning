from collections import deque

n, s = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # Создаём матрицу

graph_2 = {}


for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 1:
            if i not in graph_2:
                graph_2[i] = [j]
            else:
                graph_2[i].append(j)
# print(graph_2)

visited = set()  # Set to keep track of visited nodes of graph.


def dfs(visited_def, graph_def, node):  # function for dfs
    if node not in visited_def:
        # print(node)
        visited_def.add(node)
        if node in graph_def:
            for neighbour in graph_def[node]:
                dfs(visited_def, graph_def, neighbour)


# Driver Code
# print("Following is the Depth-First Search")
dfs(visited, graph_2, s-1)
# print(visited)
print(len(visited) - 1)

# Попытался переписать dfs на массив
# Получается там у нас по ключу(нашей вершине) выдаётся сразу её соседи в виде вершин
# Передав строчку, мы тоже можем понять соседей, если пройти вторым циклом по этой строчке и там 1, значит сосед
# Но как это переписать под такую структуру так и не понял(
# def dfs(vertex1, vertex2, graph_):
#     # used.add(vertex)
#     used[vertex1][vertex2] = True
#
#     for line_graph in graph_[vertex1]:
#         for j in
#         if not used[neighbour]:
#             dfs(neighbour, graph_)
#
#
# count = 0
# for vertex1 in range(len(graph)):
#     for vertex2 in range(vertex1, len(graph)):
#         if graph[vertex1][vertex2] == 1 and not used[vertex1][vertex2]:
#             dfs(vertex1, vertex2, graph)
#             count += 1


# def bfs(start):
#     queue = deque([start])
#     used[start] = True
#     distances[start] = 0
#     # Если длина очереди будет 0, то дальше не пойдём
#     while queue:
#         source = queue.popleft()  # Получаем вершину
#         for destination in range(n):
#             if graph[source][destination] == "1" and not used[destination]:
#                 used[destination] = True
#                 queue.append(destination)
#
#                 distances[destination] = distances[source] + 1
#
#
# bfs(s)
# print(distances)
# print(graph)

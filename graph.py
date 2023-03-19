# import queue
#
# h, w = map(int, input().split())
# # used = set()
# used = [False]*(h*w)
# def ind(i, j):
#     return (i-1)*w+j-1
# def func(i, j):
#     return 1<=i<=h and 1<=j<=w and 0 <= ind(i, j) < h*w and not used[ind(i, j)]
#
# n, *points = map(int, input().split())
#
# q = queue.Queue()
# for i in range(1, len(points), 2):
#     q.put((points[i-1], points[i], 0))
#     used[ind(points[i-1], points[i])] = True
# #Алгоритм поиска в щирину
# t = 0
# while not q.empty():
#     i, j, t = q.get()
#     for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
#         if func(x, y):
#             used[ind(x, y)] = True
#             q.put((x, y, t+1))
# print(t)

# Определение веса объекта
# import sys
# import queue
#
# q = queue.Queue()
# for i in range(100):
#     q.put((1, 2, 3))
# print(sys.getsizeof(q))
#
# q1 = queue.Queue()
# q2 = queue.Queue()
# q3 = queue.Queue()
#
# for i in range(100):
#     q1.put(1 * i)
#     q2.put(2 * i)
#     q3.put(3 * i)
# print(sys.getsizeof(q1) + sys.getsizeof(q2) + sys.getsizeof(q3))

#185

# n, k = map(int, input().split())
#
# graph = [[0]*n for i in range(n)]
# print(graph)
# inp = input()
# while inp != "0":
#     x, y = map(int, inp.split())
#     graph[x-1][y-1] = 1
#     inp = input()
# # print("update graph")
# # print(graph)
# ex = set()
#
#
# def dfs(node):
#     ex.add(node)
#     for coherence in range(len(graph)):
#         if graph[node][coherence] == 1 and coherence not in ex:
#             dfs(coherence)
#
#
# dfs(k-1)
# # print(ex)
#
# if len(ex) == n:
#     print("Yes")
# else:
#     print("No")


# ЗАДАЧА №871
# Автогонки
# n, m = map(int, input().split())
# graph = [[0]*n for i in range(n)]
# # print(graph)
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x-1][y-1] = 1
#     graph[y-1][x-1] = 1
# # print(graph)
#
# color = {}  # key: value
# for i in range(n):
#     color[i] = "white"
# # print(color)
#
#
# answer = "NO"
#
# flag = False
# def dfs(vertex, last_element):
#     global flag
#     color[vertex] = "grey"
#     for i in range(n):
#         if i == last_element:
#             continue
#         if graph[vertex][i] == 1:
#             if color[i] == "white":
#                 dfs(i, vertex)
#             if color[i] == "grey":
#                 flag = True
#     color[vertex] = "black"
#
# for i in range(n):
#     if color[i] == "white":
#         dfs(i, -1)
# print(color)

# if flag:
#     answer = "YES"
# print(answer)
# def dfs(node, last=None):
#     ex.add(node)
#     if node not in roads and last != node:
#         roads.add(node)
#         last = node
#     else:
#         answer = "YES"
#     for coherence in range(len(graph)):
#         if graph[node][coherence] == 1 and coherence not in ex:
#             dfs(coherence)

# for i in range(m):
#     x = graph[i][0]
#     dfs(x)
#     if ex == m:
#         answer = "YES"
#         break


#ЗАДАЧА №135
# Алгоритм Флойда

# # for (int k=0; k<n; ++k)
# # 	for (int i=0; i<n; ++i)
# # 		for (int j=0; j<n; ++j)
# # 			d[i][j] = min (d[i][j], d[i][k] + d[k][j]);
# n = int(input())
# d = [list(map(int, input().split())) for i in range(n)]
# # print(d)
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             d[i][j] = min(d[i][j], d[i][k] + d[k][j])
#
# for line in d:
#     print(*line)

# ЗАДАЧА №138
# Алгоритм Форда-Беллмана

# # vector <int> d (n, infinity);
# # d[0] = 0;
# # for (int k = 0; k < n - 1; k++) {
# # for (int u = 0; u < n; u++)
# # for (auto e : adj[u])
# # if (d[e.v] > d[u] + e.w)
# # d[e.v] = d[u] + e.w;
# # }
#
# n, m = map(int, input().split())
# graph = [[float("inf")]*n for i in range(n)]
# # print(graph)
# # Из вершины в саму себя вес = 0
# for i in range(n):
#     graph[i][i] = 0
#
# for i in range(m):
#     x, y, w = map(int, input().split())
#     if graph[x-1][y-1] > w:
#         graph[x-1][y-1] = w
#
# d = [float("inf")]*n
# # d = [30000]*n
# d[0] = 0
# for k in range(n-1):
#     for u in range(n):
#         for v in range(n):
#             w = graph[u][v]
#             if d[v] > d[u] + w:
#                 d[v] = d[u] + w
# for i in range(len(d)):
#     if d[i] == float("inf"):
#         d[i] = 30000
#
# for length in d:
#     print(length, end=" ")

# ЗАДАЧА №601
# Цветной лабиринт
# n, m = map(int, input().split())
# graph = [[-1]*100 for i in range(n)]
#
#
# for i in range(m):
#     x, y, color = map(int, input().split())
#     graph[x-1][color-1] = y-1
#     graph[y-1][color-1] = x-1
#
#
# route_length = int(input())
# description_route = map(int, input().split())
# current = 0
# is_exit = True
# for color in description_route:
#     color -= 1
#     if graph[current][color] != -1:
#         current = graph[current][color]
#     else:
#         is_exit = False
#         break
#
# if is_exit:
#     print(current+1)
# else:
#     print("INCORRECT")

#  136 Алгоритм Флойда
# n = int(input())  # кол-во столбцов/строк
# graph = [list(map(int, input().split())) for i in range(n)]  # построение графа
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if graph[i][j] == -1:
#             graph[i][j] = float("inf")
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# # print(graph)
# # print()
# max_value = 0
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if graph[i][j] > max_value and graph[i][j] != float("inf"):
#             max_value = graph[i][j]
# if max_value == float("inf"):
#     print(0)
# else:
#     print(max_value)

# _____________________________________
# count = 0
# while not all(sum(matrix, [])):
#     new_matrix = [matrix[i].copy() for i in range(m)]
#     for col in range(n):
#         for row in range(m):
#             if matrix[row][col]:
#                 for dc, dr in ((-1, 0), (0, -1), (1, 0), (0, 1)):
#                     c, r = col + dc, row + dr
#                     if 0 <= c < n and 0 <= r < m:
#                         new_matrix[r][c] = True
#     count += 1
#     matrix = new_matrix
#
# print(count)
# ________________________________________

# 955 Поиск в ширину
n, m = map(int, input().split())
matrix = [[False] * m for _ in range(n)]

protected, *coords = map(int, input().split())
for i in range(1, protected, 2):
    x = i-1
    y = i
    matrix[coords[x]][coords[y]] = True

# ______________________________________
n, m = map(int, input().split())
graph = {i: set() for i in range(n)}  # Создаём словарь, с ключами от 0 до n-1, а по ключу будут лежать пустые множества

# считываем все множества
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

# Расчитываем расстояние
from collections import deque
distance = [None] * n
start_vertex = 0
distance[start_vertex] = 0
queue = deque([start_vertex])

# Нахождение кротчайшего пути
parents = [None] * n  # Храним список родителей наших вершин

# Если длина очереди будет 0, то дальше не пойдём
while queue:
    cur_v = queue.popleft()  # Получаем вершину
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:
            distance[neigh_v] = distance[cur_v] + 1
            parents[neigh_v] = cur_v  # нахождение кратчайшего пути
            queue.append(neigh_v)

end_vertex = 9
path = [9]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]
# bfs - с очередью
n, m = map(int, input().split())
matrix = [[False] * n for _ in range(m)]

x, *coords = map(int, input().split())
for i in range(x):
    matrix[coords[i * 2 + 1] - 1][coords[i * 2] - 1] = True

count = 0
while not all(sum(matrix, [])):
    new_matrix = [matrix[i].copy() for i in range(m)]
    for col in range(n):
        for row in range(m):
            if matrix[row][col]:
                for dc, dr in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    c, r = col + dc, row + dr
                    if 0 <= c < n and 0 <= r < m:
                        new_matrix[r][c] = True
    count += 1
    matrix = new_matrix

print(count)







from collections import defaultdict
graph = defaultdict(list)


def addEdge(u, v):
    graph[u].append(v)

def bfs(s):
    visited = [False] * (max(graph) + 1)
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True














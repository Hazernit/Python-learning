n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

color = {}
for i in range(n):
    color[i] = "white"
# print(color)
flag = False
visited = []
def dfs(vertex, last_element):
    global flag
    color[vertex] = "grey"
    visited.append(vertex)
    for i in range(n):
        if i == last_element:
            continue
        if graph[vertex][i] == 1:
            if color[i] == "white":
                dfs(i, vertex)
            if color[i] == "grey":
                flag = True
    color[vertex] = "black"

dfs(0, -1)
# print(visited)
# print(flag)
# print(color)
if not flag and len(visited) == n:
    print("YES")
else:
    print("NO")










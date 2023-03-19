graph = {}

n = int(input())
for _ in range(n):
    a, b = input().split(" -> ")
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
start = input()
finish = input()


visited = set()  # Set to keep track of visited nodes of graph.

count = 0
flag = True
isCheck = False
def dfs(visited_def, graph_def, node):  # function for dfs
    global count
    global flag
    global isCheck
    if node not in visited_def:
        # print(node)
        visited_def.add(node)
        if node in graph_def:
            if flag:
                count += 1
            for neighbour in graph_def[node]:
                if neighbour == finish:
                    flag = False
                    isCheck = True
                dfs(visited_def, graph_def, neighbour)


dfs(visited, graph, start)
# print(visited)
if isCheck:
    print(count-1)
else:
    print(-1)

# count = 0
# for val in visited:
#     count += 1
#     print(val, finish)
#     if val == finish:
#         break
# print(count)


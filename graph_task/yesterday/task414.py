from collections import deque
n = int(input())
check_one, check_two = map(int, input().split())
# graph = [list("0" for _ in range(n)) for _ in range(n)]  # Создаём матрицу
# print(graph)
departments = list(map(int, input().split()))
# print(departments)

used = [False]*n

visited = check_one-2
while visited != -1:
    used[visited+1] = True
    visited = departments[visited]-2

visited = check_two-2
while visited != -1:
    if used[visited+1]:
        break
    visited = departments[visited]-2


print(visited+2)


# for i in range(check_one,):
#     i -= 2
#     visited = departments[i]
#     print(visited)
#     used[visited] = True
# print(used)
# answer = 0
# for i in range(check_two, n):
#     i -= 2
#     visited = departments[i]
#     if used[visited]:
#         answer = visited
#         break
# print(answer)










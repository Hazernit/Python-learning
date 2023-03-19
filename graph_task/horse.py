# Конь
letters = 'abcdefgh'
numbers = '12345678'

graph = dict()
# Создаём вершины
for i in letters:
    for n in numbers:
        graph[i+n] = set()


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        v2 = ''
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i+2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i-2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i+1] + numbers[j+2]
            add_edge(v1, v2)
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i-1] + numbers[j+2]
            add_edge(v1, v2)

print(graph)
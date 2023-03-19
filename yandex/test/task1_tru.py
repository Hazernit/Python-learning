from collections import Counter

with open('input.txt') as fin:
    data = fin.read()

for char in ' \n':
    data = data.replace(char, '')

counts = Counter(data)

max_value = max(counts.values())

chars = ''.join(sorted(set(data)))

matrix = [[' '] * len(chars) for _ in range(max_value)]

for j, char in enumerate(chars):
    count = counts[char]
    for i in range(max_value - 1, max_value - count - 1, -1):
        matrix[i][j] = '#'

for line in matrix:
    print(''.join(line))

print(chars)
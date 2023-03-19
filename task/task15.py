
n = int(input())

count = 0
for i in range(n):
    inp = list(map(int, input().split()))
    for number in inp:
        if number > 0:
            count += 1

answer = count // 2
print(answer)


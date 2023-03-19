n: int = int(input())

growths = list(map(int, input().split()))

odd = 0
honest = 0

first_wrong_index = -1
second_wrong_index = -1


for i in range(len(growths)):
    if i % 2 == 0 and growths[i] % 2 == 0:
        honest += 1
        first_wrong_index = i + 1
    elif i % 2 != 0 and growths[i] % 2 != 0:
        odd += 1
        second_wrong_index = i + 1

if odd != 1 or honest != 1:
    print(-1, -1)
else:
    print(first_wrong_index, second_wrong_index)






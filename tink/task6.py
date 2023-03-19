import math

n: int = int(input())

growths = list(map(int, input().split()))

should_be_odd = math.ceil(len(growths) / 2)
should_be_honest = len(growths) - should_be_odd

odd = 0
honest = 0

for growth in growths:
    if growth % 2 == 0:
        honest += 1
    else:
        odd += 1

index = 1
index1 = -1
index2 = -1
isOddIndex = False
if should_be_honest != honest or should_be_odd != odd:
    print(index1, index2)
else:
    for i in range(len(growths)):
        index += i
        number = growths[i]
        if index1 == -1 and (number % 2 == 0 and index % 2 != 0):
            index1 = index
            isOddIndex = True
        elif index1 == -1 and (number % 2 != 0 and index % 2 == 0):
            index1 = index
            isOddIndex = False
        elif index1 != -1 and isOddIndex and number % 2 != 0:
            index2 = index
            break
        elif index1 != -1 and not isOddIndex and number % 2 == 0:
            index2 = index
            break
    print(index1, index2)







 

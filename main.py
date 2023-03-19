# n = int(input())
# k = int(input())
#
# countSquare = n//k
# countLine = countSquare - 1
# allCountLine = countLine * 2
# glue = allCountLine * n
# print(glue)

#
# x = int(input())
# y = int(input())
# n = int(input())
#
# doubleJump = x + y
# countDoubleJump = n // doubleJump
# lineCountJump = countDoubleJump * doubleJump
#
# remains = n - lineCountJump
# countJump = countDoubleJump * 2
# if remains <= y:
#     countJump += 1
# else:
#     countJump += 2
# print(countJump)

# TODO 3
# start_s = int(input())
# finish_e = int(input())
# countN = int(input())
# lineTeleport = []
# for i in range(countN):
#     n = int(input())
#     lineTeleport.append(n)
# distanceStraight = finish_e - start_s
# lineDistanceForTeleport = []
# for i in lineTeleport:
#     distanceIforTeleport = abs(i-start_s)
#     lineDistanceForTeleport.append(distanceIforTeleport)
# minlineDistanceForTeleport = min(lineDistanceForTeleport)
# lineDistanceAfterTeleport = []
# for i in lineTeleport:
#     distanceAfterTeleport = abs(finish_e - i)
#     lineDistanceAfterTeleport.append(distanceAfterTeleport)
# minDistanceAfterTeleport = min(lineDistanceAfterTeleport)
# distanceUsedTeleport = minlineDistanceForTeleport + 1 + minDistanceAfterTeleport
# if distanceStraight < distanceUsedTeleport:
#     answer = distanceStraight
# else:
#     answer = distanceUsedTeleport
# print(answer)


# TODO 4
# quantityLian = int(input())
# staticDistance = int(input())
#
# maxCoord = 0
#
# for i in range(quantityLian):
#     if staticDistance*i > maxCoord:
#         print(i)
#         break
#     distanceLian = int(input())
#     distance = staticDistance * i + distanceLian
#     if maxCoord <= distance:
#         maxCoord = distance
# else:
#     print(quantityLian)


# 5 TODO
# не очень понял что за N нужно подобрать
# Нам придётся в первом случае N = 1 ?)
# Если да, то почему ответ 10 ?)

# 1
# k = int(input())
# n = int(input())
#
# multiplier = n // k
#
# busStopA = (multiplier-1)*k
# busStopB = multiplier*k
# busStopC = (multiplier+1)*k
#
# distanceA = abs(n - busStopA)
# distanceB = abs(n - busStopB)
# distanceC = abs(busStopC-n)
# answer = min(distanceA, distanceB, distanceC)
# print(answer)

# 2
# croissants = int(input())
# eclairs = int(input())
# result = -1
#
# total = croissants + eclairs
# if croissants < eclairs and total % 3 == 0:
#     print((total//3)-2, (total//3)-1)
# elif croissants > eclairs and total % 3 == 0:
#     print((total//3)-1, (total//3)-2)
# elif croissants == eclairs and total % 3 == 0:
#     print(total//3, total//3)
# elif total % 3 != 0:
#     print(result)

# 3
# sizeBoard = int(input())
#
#
# lineSizeBoard = [0]*sizeBoard
# for i in range(sizeBoard):
#     horizon = i+1
#     vertical = int(input())
#
#     horizon, vertical = vertical, (sizeBoard+1)-horizon
#     lineSizeBoard[horizon-1] = vertical
# print(lineSizeBoard)


# 4
# Нашёл только то, что сначала на одну увеличивается правое число
# затем левое увеличивается на 1 до тех пор, пока не станет равным строке
# затем уменьшается строка на 1 до тех пор, пока не станет равна 1
# затем увеличивается столбец на один и строка
# увеличивается на 1 до тех пор пока не станет равной столбцу
# Код скопировал, но не понял(


# 11 -> 1
# 12 -> 2
# 22 -> 3
# 21 -> 4
# 31 -> 5
# 32 -> 6
# 33 -> 7
# 23 -> 8
# 13 -> 9
# 14 -> 10
# 24 -> 11
# 34 -> 12
# 44 -> 13
# 43 -> 14
# 42 -> 15
# 41 -> 16
# 51 -> 17
# 52 -> 18
# 53 -> 19
# 54 -> 20
# 55 -> 21
# 45 -> 22
# def check(x, y, n):
#     if n == 0:
#         print(y, x)
#
# n = int(input())-1
# x = 1
# y = 1
# step = 1
# while n > 0:
#     x += 1
#     n -= 1
#     check(x, y, n)
#     for i in range(step):
#         y += 1
#         n -= 1
#         check(x, y, n)
#     for i in range(step):
#         x -= 1
#         n -= 1
#         check(x, y, n)
#     step += 1
#     y += 1
#     n -= 1
#     check(x, y, n)
#     for i in range(step):
#         x += 1
#         n -= 1
#         check(x, y, n)
#     for i in range(step):
#         y -= 1
#         n -= 1
#         check(x, y, n)
#     step += 1

# def integerSqrt(n):
#     if n < 2:
#         return n
#     else:
#         smallCandidate = integerSqrt(n >> 2) << 1  # что значит >>
#         largeCandidate = smallCandidate + 1
#         if largeCandidate * largeCandidate > n:
#             return smallCandidate
#         else:
#             return largeCandidate
#
#
# n = int(input())
# m = integerSqrt(n - 1)
# k = (m * (m + 1) + 1)
# if m % 2 == 1:
#     if k < n:
#         row = m + 1
#         col = (m + 1) - (n - k)
#     elif k == n:
#         row = m + 1
#         col = m + 1
#     else:
#         col = m + 1
#         row = (m + 1) + (n - k)
# else:
#     if k < n:
#         col = m + 1
#         row = (m + 1) - (n - k)
#     elif k == n:
#         row = m + 1
#         col = m + 1
#     else:
#         row = m + 1
#         col = (m + 1) + (n - k)
# print(row, col)


# [1, 1, 5, 5, 7, 11]
# [0, 0, 1, 1, 1, 1]
# [1, 3, 4, 11, 15]
# [0, 1, 0, 1, 1]
# users = int(input())
#
# lineSize = []
# for i in range(users):
#     lineSize.append(int(input()))
#
# line = [1]*users
# size = 0
# for i in range(users-1):
#     size += lineSize[i]
#     if size <= lineSize[i+1]:
#         line[i] = 0
#
# start = 0
# for i in range(len(line)):
#     if line[i] == 0:
#         start = i
# for i in range(start):
#     line[i] = 0
#
# print(line)


# dictionaryUserSize = {}
# for i in range(users):
#     dictionaryUserSize[i] = int(input())
# for user, size in dictionaryUserSize.items():
#     allSizeline = []
#     allSizeline.append(size)
#
# minSize = min(allSizeline)
# maxSize = max(allSizeline)
#
# for i in range(users):
#     if dictionaryUserSize[i] == minSize:
#         dictionaryUserSize[i] = 0

# TODO 1
# a = int(input())
# b = int(input())
#
# x = (a-1)//2
# y = (b-1)//2
# answer = abs(y -x)
# print(answer)

# n = 0
# if a > b:
#     a, b = b, a

# for i in range(a, b+1):
#     if a % 2 != 0:
#         if i % 2 != 0:
#             if b - i == 3:
#                 print(i)
#                 print(i + 3)
#                 break
#             print(i)
#     else:
#         if i % 2 == 0:
#             if b - i == 1:
#                 print(i)
#                 print(i + 1)
#                 break
#             print(i)

# код
# count = -1
# for i in range(a, b+1):
#     if a % 2 != 0:
#         if i % 2 != 0:
#             if b - i == 3:
#                 count += 2
#                 break
#             count += 1
#     else:
#         if i % 2 == 0:
#             if b - i == 1:
#                 count += 2
#                 break
#             count += 1
# print(count)


# for i in range(a, b):
#     if b - i == 2:
#         print(i + 2)
#         break
#     if a % 2 != 0:
#         if (b-i) != 3:  # Почему при не выполнении условия код всё равно выполняется
#             print(f"b - i = {b-i}")
#             if i % 2 != 0:
#                 print(i)
#         else:
#             print(i)
#             print(i+3)
#             break
#     else:
#         if b - i != 3 and b - i != 2:
#             print(f"b - i = {b-i}")
#             if i % 2 == 0:
#                 print(i)
#         else:
#             print(i)
#             print(i-3)


# count = -1 # т.к считаем начальную точку
# for i in range(a, b):
#     if b - i == 2:
#         count += 2
#         break
#     if a % 2 != 0:
#         if (b-i) != 2 and (b-i) != 3:  # Почему при не выполнении условия код всё равно выполняется
#             if i % 2 != 0:
#                 count += 1
#         else:
#             count += 2
#             break
# print(count)


# for i in range(1, b):
#     print(i)
#     print(f"b -i = {b-i}")
#     x = i+1
#     if a % 2 == 1:
#         if i
#         if b - i == 3 or b - i == 2:
#             n += 1
#             break
#         else:
#             n += 1
# print(n)

# TODO 2
# a = int(input())
# b = int(input())
# c = int(input())
# minNumber = min(a, b, c)
# maxNumber = max(a, b, c)
#
# answer = (a + b + c) - (maxNumber+minNumber)
#
# print(answer)

# TODO 3
# m = int(input())
#
# i = 1
# answer = -1
# while (i*i) <= m:
#     if m % (i*i) == 0:
#         answer = i * i
#     i += 1
# print(answer)

# TODO 4

# до 2: -1+2 = -1 (-)
# до 3: -1-2+3 = 0 (+)
# до 4: +1-2-3+4 = 0 или -1+2+3-4 = 0 (+)
# до 5: -1-2-3-4+5  = -3 или +3 (-)
# до 6: -1-2-3-4-5+6 = -1 или +1 (-)
# до 7: -1-2-3-4-5-6+7 = -8 или +8 (-)
# до 8: -1-2-3-4-5-6-7+8 = -20

# n = int(input())
# a = "--+"
# b = "+--+"
# m = n // 4
# answer = "IMPOSSIBLE"
# if n % 4 == 0:
#     answer = b*m
# elif n % 4 == 3:
#     answer = a+b*m
# print(answer)

# +--+ - если ост 0 при делении кол-во чисел на 4
# --+ - если ост 3 при делении кол-во чисел на 4

# TODO 5
# line = input().lower()
#
# answer = ""
# number = ""
# totalX = 0  # Сервер, ЮГ
# totalY = 0  # Запад, Восток
# for i in range(len(line)):
#     if line[i].isdigit():
#         number += line[i]  # "7"+"2" = "72"
#     else:
#         if 's' in line[i]:
#             totalX += int(number)
#         if 'n' in line[i]:
#             totalX -= int(number)
#         if 'w' in line[i]:
#             totalY += int(number)
#         if 'e' in line[i]:
#             totalY -= int(number)
#         number = ""
#
# print(totalX, totalY)
#
# if totalX < 0:
#     totalX = abs(totalX)
#     answer += str(totalX)+"N"
# else:
#     answer += str(totalX)+"S"
#
# if totalY < 0:
#     totalY = abs(totalY)
#     answer += str(totalY)+"E"
# else:
#     answer += str(totalY)+"W"
#
# print(answer)


# a = "3b"
# for i in range(len(a)):
#     print(a[i].isdigit())


# for i in range(len(line)):
#     if 's' in line[i] or 'n' in line[i]:
#         for j in line[i]:
#             if j.isdigit():
#                 j = int(j)
#                 totalX += j
#     else:
#         for j in line[i]:
#             if j.isdigit():
#                 j = int(j)
#                 totalY += j-1
# print(totalX, totalY)


# 1 Спинеры

# a, b, c = map(int, input().split())
#
# total = 0
# blade = 0
# while total <= c:
#     blade += 1
#     total = b * blade + a
#
# answer = blade - 1
# print(answer)
# answer2 = (c-a)//b
# print(answer2)

#
#
# print(answer)


# 2 Снова спинеры (Смотрел решение)

# blade = int(input())
#
# four = blade % 3
# three = (blade - four*4) // 3
#
# if blade == 1 or blade == 2 or blade != four*4 + three*3:
#     print(0)
#     print(0)
# else:
#     print("троек: "+str(three))
#     print("четвёрок: "+str(four))

# 3
# Пронумеруем столбцы листа числами от 1 до N, строки листа числами от 1 до M.
# Пусть клетка, находящаяся в одном углу прямоугольника имеет координаты x1, y1, а
# противоположная клетка — координаты x2, y2. Тогда выполнены неравенства 1 ≤ x1 ≤ x2 ≤ N,
# 1 ≤ y1 ≤ y2 ≤ M. Задача сводится к подсчёту количества четвёрок чисел x1, y1, x2, y2,
# удовлетворяющих этим неравенствам.
# Если это делать при помощи четырёх циклов, то получится решение сложности
# O(N
# 2M2
# ), которое набирает 40 баллов. Пример такого решения.
# n = int(input())
# m = int(input())
# ans = 0
# for x1 in range(n):
#  for x2 in range(x1, n):
#  for y1 in range(m):
#  for y2 in range(y1, m):
#  ans += 1
# print(ans)
# Для получения больших баллов необходимо оптимизировать это решение. Например,
# можно заметить, что задачу можно решать независимо по каждой из двух осей координат, то
# есть нужно подсчитать количество подходящих пар x1, x2 и количество подходящих пар y1, y2
# и перемножить два найденных числа. Такое решение будет иметь сложность O(N
# 2 + M2
# ) и
# набирает 70 баллов. Пример такого решения:
# n = int(input())
# m = int(input())
# ans_x = 0
# ans_y = 0
# for x1 in range(n):
#  for x2 in range(x1, n):
#  ans_x += 1
# for y1 in range(m):
#  for y2 in range(y1, m):
#  ans_y += 1
# print(ans_x * ans_y)
# Для дальнейшего улучшения решения заметим, что во вложенных циклах к числу
# прибавляется 1, поэтому можно оба вложенных цикла заменить на увеличение переменной
# на число, равное количеству итераций вложенного цикла. Такое решение будет иметь
# сложность O(N + M) и набирает 100 баллов. Пример такого решения:
# n = int(input())
# m = int(input())
# ans_x = 0
# ans_y = 0
# for x1 in range(n):
#  ans_x += n - x1
# for y1 in range(m):
#  ans_y += m - y1
# print(ans_x * ans_y)
# Это решение уже набирает полный балл, но и его можно упростить, если заметить,
# что в первом цикле суммируются числа n + (n – 1) + … + 1, и эта сумма равна n (n + 1) / 2.
# Аналогично, сумма чисел во втором цикле равна m (m + 1) / 2. Можно перемножить эти два
# числа, получится решение сложности O(1). Пример такого решения:
# n = int(input())
# m = int(input())
# print(n * (n + 1) // 2 * m * (m + 1) // 2)

# a = int(input())
# b = int(input())
#
# array = []
# for i in range(2):
#     newArray = []
#     print()
#     for j in range(5):
#         newArray.append(j)
#         print(j, end=" ")
#     array.append(newArray)
#
#
#
# print()
# for i in range(1, len(array)):
#     print()
#     for j in range(len(newArray)):
#         print(newArray[j], end=" ")
#         print(array[i][j] == array[i-1][j])

# count = 0
# for y in range(len(array)):
#     for x in range(len(newArray)):
#         for _ in range(x, len(newArray)):
#             count += 1
#             if _ == newArray[-1]:
#                 break
#             print(f"x: {x}", end=" ")
#             print()
#             print(f"_: {_}", end=" ")
# print("test")
# width = int(input())
# height = int(input())
# count = 0
# for filled_width in range(1, width+1):
#     for filled_height in range(1, height+1):
#         count_vertical = height - filled_height + 1  # сколькими различными способами можем двигать по вертикали
#         count_horizontal = width - filled_width + 1  # сколькими различными способами можем двигать по горизонтали
#         count += count_horizontal * count_vertical
# print(count)

# 4 Ошибка
# countFreePlaces = int(input())
# freePlaces = []
# for _ in range(countFreePlaces):
#     place = int(input())
#     freePlaces.append(place)
#
# freePlaces = sorted(freePlaces)
#
# print(freePlaces)
# onePartWagon = []
# twoPartWagon = []
# for i in freePlaces:
#     if i <= 36:
#         onePartWagon.append(i)
#     else:
#         twoPartWagon.append(i)
#
# arrayIndex = []
# for i in range(3, len(onePartWagon)):
#     if onePartWagon[i-3] == onePartWagon[i-2]-1 and onePartWagon[i-2] == onePartWagon[i-1]-1 and onePartWagon[i-1] == onePartWagon[i]-1:
#         index = onePartWagon[i] // 4
#         arrayIndex.append(index)
# for i in range(1, len(twoPartWagon)):
#     if twoPartWagon[i-1] == twoPartWagon[i]-1:
#         index = twoPartWagon[i]//2 - 9
#         arrayIndex.append(index)
#
# answer = 0
# for i in range(1, len(arrayIndex)):
#     if arrayIndex[i-1] == arrayIndex[i]-1:
#         answer += 1
# if len(arrayIndex) >= 1 and answer != 0:
#     answer = 1
# print(answer)

# quantityPlaceCoupe = [0]*18 # 1-8 13-24 29-36 37-40 43-48 51-54
# n = int(input())
# for _ in range(n):
#     place = int(input())
#     if place <= 36:
#         van = (place-1) // 4  # Номер вагона для 4 мест
#         quantityPlaceCoupe[van] += 1
#     else:
#         van = abs((place-1) // 2 - 26) # Номер вагона для двух мест
#         quantityPlaceCoupe[van] += 1
# countFreeVan = 0
# countFreeVanMax = 0
# for i in range(len(quantityPlaceCoupe)):
#     if quantityPlaceCoupe[i] == 6:
#         countFreeVan += 1
#         if countFreeVan > countFreeVanMax:
#             countFreeVanMax = countFreeVan
#     else:
#         countFreeVan = 0
# print(countFreeVanMax)


# 1
# cost = int(input())
# percent = int(input())
# money = int(input())
#
# newCost = cost + ((cost/100)*percent)
# print(newCost)
# quantity = money//newCost
# print(int(quantity))


# 2 Плот

# southWestX1 = int(input()) # Юго-запад
# southWestY1 = int(input())
#
# northEastX2 = int(input()) # Северо-восток
# northEastY2 = int(input())
#
# swimmerX = int(input())
# swimmerY = int(input())
#
# southEastX3 = northEastX2 # Юго-восток
# southEastY3 = southWestY1
#
# northWestX4 = southWestX1 # Северо-запад
# northWestY4 = northEastY2
#
# answer = ''
# if swimmerY > northEastY2:
#     if swimmerX > northEastX2:
#         answer = "NE"
#     else:
#         answer = "NW"
# else:
#     if swimmerX > southEastX3:
#         answer = "SE"
#     else:
#         answer = "SW"
# print(answer)

# нужно сопоставить, но как

# 3
# weightMax = int(input())
# quantityThings = int(input())
# allThings = []
# for i in range(quantityThings):
#     thing = int(input())
#     allThings.append(thing)
#
# backpack = []
# bag = []
# for weightThing in allThings:
#     if weightThing <= weightMax:
#         backpack.append(weightThing)
#         weightMax -= weightThing
#     else:
#         bag.append(weightThing)
# print(sum(bag))
# print(sum(backpack))


# 4
# print(4)
#
# quantity = int(input())
#
# dots = []
# for _ in range(quantity):
#     dot = int(input())
#     dots.append(dot)
# if max(dots) > dots[0] > min(dots):
#     for i in range(1, len(dots)):
#         if dots[i] == max(dots):
#             startIndex = i-1
#         if dots[i] == min(dots):
#             finishIndex = i
#     print(startIndex)
#     print(finishIndex)
# else:
#     print(0)


# 1 Считалка

# n = int(input())
# m = int(input())
# answer = (m-1) % n + 1
# print(answer)

# 2 Конфеты

# numbers = [1, 2, 3, 4]
#
# i = 0
# di = 1
#
# for _ in range(10):
#     print(numbers[i], end=" ")
#     i += di
#     if i == len(numbers) - 1 or i == 0:
#         di = -di
#
# print()
# sweet1 = int(input())
# sweet2 = int(input())
# sweet3 = int(input())
# sweets = {0: sweet1, 1: sweet2, 2: sweet3}
# numbers = [0, 1, 2] # 0 1 2 1 0 1 2 1
# numbers = [sweet1, sweet2, sweet3]
# i = 0
# di = 1
# count = 0
#
# while numbers[i] != 0:
#     print(numbers[i], end=" ")
#     numbers[i] -= 1
#     count += 1
#     i += di
#     if i == len(numbers) - 1 or i == 0:
#         di = -di
# print()
# print(count)

# for _ in range(sweet1*sweet2*sweet3):
#     print(numbers[i], end=" ")
#     i += di
#     count += 1
#     if sweets[i] > 0:
#         sweets[i] -= 1
#     else:
#         break
#     if i == len(numbers) - 1 or i == 0:
#         di = -di

# sweet1 = int(input())
# sweet2 = int(input())
# sweet3 = int(input())
# arraySweets = [sweet1, sweet2, sweet3]
# count = 0
# index = 0
# arrayIndex = [index]
# while arraySweets[index] != 0:
#     arraySweets[index] -= 1
#     count += 1
#     if arraySweets[index] > 0 and index+1 == 2:
#         index += 1
#         arrayIndex.append(index)
#     elif arraySweets[index] > 0 and arrayIndex[-1] == 1 and arrayIndex[-2] == 0:
#         index = 2
#         arrayIndex
#     elif arraySweets[index] > 0 and arrayIndex[-1] == 2 and arrayIndex[-2] == 1:
#         index = 1
#     elif arraySweets[index] > 0 and arrayIndex[]

# 3 Расписание кружка
# print("test 3")

# month = int(input())
# day = int(input())
# print(month, day)
#
#
# def out_put(month, day):
#     if month <= 12:
#         print(month, day)
#
#
# def dayInMonth(month):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month in (4, 6, 9, 11):
#         return 30
#     elif month in 2:
#         return 28
#
# while month <= 12:
#     day += 7
#     if day > dayInMonth(month):
#         day -= dayInMonth(month)
#         month
#     out_put(month, day)


# 4 Кратное трём число
# print("test 4")
# test = list(input())
# digit = test[0]
# digit -= 1   # Почему-то нельзя обернуть в int
# test[0] = digit
# print(test)

# number = list(input())
# count = len(number)    # Если сумма делится на 3, то и число делится, как найти макс сумму
# i = 0
# flag = False
# while i < count:
#     for _ in range(len(number)):
#         before = number[i]
#         number[i] = "9"
#         while number[i] >= "0" and not flag:
#             if int("".join(number)) % 3 != 0:
#                 digit = int(number[i])
#                 digit -= 1
#                 number[i] = str(digit)
#             else:
#                 print("".join(number))
#                 flag = True
#         if flag:
#             break
#         number[i] = before
#         i += 1


# TODO 5
# n = int(input())
# arrayNumbers = []
# for _ in range(n):
#     digit = int(input())
#     arrayNumbers.append(digit)
#
# arrayNumbers = sorted(arrayNumbers, reverse=True)
# answer = 0
# flag = True
# # если все положительные и последний элемент не 0, то его можно не искать
# for i in range(len(arrayNumbers)):
#     if arrayNumbers[i] == 0:
#         answer = 0
#         flag = False
#         break
# if flag:
#     if arrayNumbers[-1] < 0 and arrayNumbers[0] > 0:
#         answer = arrayNumbers[0] * arrayNumbers[-1]
#     elif arrayNumbers[-1] > 0 and arrayNumbers[0] > 0:
#         answer = arrayNumbers[-1] * arrayNumbers[-2]
#     elif arrayNumbers[0] < 0 and arrayNumbers[1] < 0:
#         answer = arrayNumbers[0] * arrayNumbers[1]
# print(answer)

# 1 Шахматная доска
# print("Шахматная доска")
# n = int(input())
# m = int(input())
# answer = (n*m)//2
# print(answer)

# 2 Манхэттен
# print("Манхэттен")
#
# startX = int(input())
# startY = int(input())
#
# finishX = int(input())
# finishY = int(input())
#
# rightE = 0                # E
# while finishX > startX:
#     rightE += 1
#     startX += 1
#     print(1)
#
# upN = 0                  # N
# while finishY > startY:
#     upN += 1
#     startY += 1
#     print(2)
#
# leftW = 0              # W
# while startX > finishX:
#     leftW += 1
#     startX -= 1
#     print(3)
#
# downS = 0               # S
# while startY > finishY:
#     downS += 1
#     startY -= 1
#     print(4)
#
# print("E"*rightE+"S"*downS+"W"*leftW+"N"*upN)

# 3 Пятница, 13-е
# print("Пятница, 13-е")
# 60 - вторник
# print(42//7)
# month_in_year = int(input())
# firstDay_firstMonth = int(input())
#
# friday = firstDay_firstMonth + 5  # Пятница
# day_in_year = month_in_year * 30
#
# count = 0
# if day_in_year == 2:
#     count += 1
#
# dayOfWeek = (13 - day_in_year)-1 % 7  # День Недели
#
# thisMonth = 1
# while month_in_year > thisMonth:
#     print(1)
#     dayOfWeek += 30 // 7
#     if dayOfWeek == 6:
#          count += 1
#     thisMonth += 1

# print(count)
# # day_of_week = (30 - 1) % 7 + 1
# N = int(input())
# k = int(input())
# ans = 0
# k = (k + 12) % 7  # Номер дня
# for i in range(N):
#     if k == 5:
#         ans += 1
#     k = (k + 30) % 7
# print(ans)


# 4
# print("Автомобильные номера")
# import re
#
# flag = True
# line = input()
# if re.fullmatch(r'[A-Z]\d{3}\w{2}', line):
#     print(1)
# elif re.fullmatch(r'[A-Z]{2}\d{3}', line):
#     print(2)
# elif re.fullmatch(r'[A-Z]{2}\d{4}', line):
#     print(3)
# elif re.fullmatch(r'\d{4}[A-Z]{2}', line):
#     print(4)
# else:
#     print(0)

# Нужно проверить последовательность букв..

# 5
# number = int(input())
#
# i = 0
# numberOur = 0
# while number > i:
#     numberOur += 1
#     number = str(number)
#     if len(number) == 1:
#         i += 1
#         numberOur += 1
#     elif number == number[::-1]:
#         i += 1
#     numberOur += 1


# 1 Цепь
# print("Цепь")
# d = int(input())
# r = int(input())
# n = int(input())

# Я не определился) Либо для двух индивидуальная формула:
# ((2*r)*2, мы должны не посчитать радиусы внешние и вычесть из внутренних радиусов внешние
# if n == 1:
#     answer = 2*d + 2*r
# else:
#     answer = ((n-1) * (2*r + 2*d)) + (2*r - 2*d)
# print(answer)


# 2 Лифт
# print("Лифт")
# current_floor = int(input())
# down_floor = int(input())
# up_floor = int(input())
#
# if current_floor - down_floor < 0:
#     answer = current_floor - down_floor - 1
# if current_floor - down_floor < 0 and (current_floor - down_floor) + up_floor > 0:
#     answer += up_floor + 1
# else:
#     answer = current_floor - down_floor + up_floor
# print(answer)

# 3 Длинное число
# print("Длинное число")
# number = list(input())
# length_number = len(number)
# # print(number)
#
# # сколько всего точек:
# total_dot = length_number // 3
# # print(length_number)
# # print(total_dot)
#
# # через сколько цифр первая точка
# first_dot = length_number % 3
# if first_dot > 0:
#     number.insert(first_dot, ".")
#     index = first_dot
#     total_dot -= 1
# else:
#     index = -2
# while total_dot > 0:
#     index += 4   # подбором получилось +4, а почему
#     number.insert(index, ".")
#     total_dot -= 1
# print(*number)

# 4 Сумма цифр ?
# print("Сумма цифр")
# start = int(input())
# finish = int(input())
#
# count = 0
#
# for number in range(start, finish+1):
#     number = str(number)
#     total = 0
#     for digit in number:
#         total += int(digit)
#     if total % 2 == 0:
#         count += 1
# if start == finish and start % 2 == 0:
#     count = 0
# print(count)

# 1 Сокращаем перемены
# print("Сокращаем перемены")
#
# count_lessons = int(input())
# answer = (count_lessons-1) * 5
# print(answer)

# 2 Шестеренки
# print("Шестеренки")


# TODO 3 Инопланетянин» не получилась
# # print("Инопланетянин»")
# #
# #
# def func10(answer, number_system):
#     answer = answer[::-1]
#     # print(answer)
#     result = 0
#     index = 0
#     for symbol in answer:
#         if symbol.isalpha():
#             k = ord(symbol) - ord("A") + 10
#         else:
#             k = int(symbol)
#         result += number_system ** index * k
#         index += 1
#     return result
#
# def maxDigit(a):
#     maxK = 0
#     for symbol in a:
#         if symbol.isalpha():
#             k = ord(symbol) - ord("A") + 10
#         else:
#             k = int(symbol)
#         if maxK < k:
#             maxK = k
#     return maxK
#
#
# a, b, result = input().split()
#
# maxNumber = max(maxDigit(a), maxDigit(b), maxDigit(result))
#
#
# # print(func10(1101010, 2))
#
#
#
# answer = -1
# for system_number in range(maxNumber+1, 100):
#     if func10(a, system_number) + func10(b, system_number) == func10(result, system_number):
#         answer = system_number
#         break
# print(answer)

# 4 «Распаковка строчки»
# print("«Распаковка строчки»")
# test = "a"
# print(test*4)
#
# line = input()
#
# new_line = ""
# number = ""
# for i in range(len(line)):
#     # Если начинаем с цифры, то условие для одиночной буквы будет такое
#     if line[i].isdigit():
#         number += line[i]
#     else:
#         if number != "":
#             new_line += int(number) * line[i]
#         else:
#             new_line += line[i]
#         number = ""
# print(new_line)
# print("DDDDDDDDDDDDDDDDDDDDDDAAAAAAACFFFFFFFFFFFFFFFFFFGD"=="DDDDDDDDDDDDDDDDDDDDDDAAAAAAACFFFFFFFFFFFFFFFFFFGD")

# 5 «Жизнь в квадрате»
# square, t = map(int, input().split())
#
# array = []
# for i in range(square):
#     row = list(map(int, input().split()))
#     array.append(row)
#
# new_array = [[0]*square for i in range(square)]
# for _ in range(t):
#     for i in range(square):
#         for j in range(square):
#             count = 0
#             for ii in range(i-1, i+2):
#                 for jj in range(j-1, j+2):
#                     if (ii != i or jj != j) and 0 <= ii < square and 0 <= jj < square:
#                         count += array[ii][jj]
#
#             if count < 2 or count > 3:
#                 new_array[i][j] = 0
#
#             if count >= 3:
#                 new_array
# print(array)


# for column in range(1, len(array)):
#     for row in range(1, column):
#         count = 0
#         if array[row][column] != 0:
#             # левая сторона
#             if array[row-1][column] == 1:
#                 count += 1
#             # левый угол
#             if array[row-1][column-1]:
#                 count += 1
#             # вверх
#             if array[row][column+1]:
#                 count += 1
#             # правый угол
#             if array[row+1][column+1]:
#                 count += 1
#             # правая сторона
#             if array[row+1][column]:
#                 count += 1
#             # правый нижний угол
#             if array[row+1][column-1]:
#                 count += 1
#             # низ
#             if array[row][column-1]:
#                 count += 1
#             # левый нижний угол
#             if array[row-1][column-1]:
#                 count += 1


# 1 Сумма прописью
# print("Сумма прописью")
#
# def word_number(number):
#     zero = ["ноль"]
#     array_digit = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
#     array_number = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
#                     "семнадцать", "восемнадцать", "девятнадцать"]
#     array_dozens = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
#     array_hundreds = ["сто", "двести"]
#
#     if len(number) > 1:
#         number = number[::-1]
#         print(number)
#         a_word = ""
#         count = 0
#         if 10 <= int(number) < 20:
#             word = int(a_word[0])
#             a_word = array_number[word]
#         else:
#             for word in number:
#                 word = int(word)
#                 if count == 0 and word != 0:
#                     a_word += array_digit[word - 1]
#                 elif count == 1 and word != 0:
#                     a_word += " " + array_dozens[word - 2]
#                 elif count == 2 and word != 0:
#                     a_word += " " + array_hundreds[word - 1]
#                 count += 1
#         finish_a_word = ""
#         a_word = list(a_word.split())
#         for word in range(len(a_word) - 1, -1, -1):
#             finish_a_word += " " + a_word[word]
#         return finish_a_word.replace(" ", "", 1)
#
# a, b = input().split()
#
#
# result = int(a) + int(b)
#
# print(word_number(a) + " плюс " + word_number(b) + " равно " + word_number(str(result)))

# test = input()
# test = list(test.split())
# for i in range(len(test)-1, -1, -1):
#     print(test[i])


# 2  Угадай число
# print("Угадай число")
#
# minNumber = 1
# maxNumber = 100
#
# line = input()
# for i in range(len(line)):
#     answer = round((minNumber + maxNumber)/2)
#     if line[i] == ">":
#         minNumber = answer
#     elif line[i] == "<":
#         maxNumber = answer
#     elif line[i] == "=":
#         print(answer)
#         break

# 3 Ступеньки
# print("Ступеньки")
#
# n, m, k = map(int, input().split())
#
# flag = True
#
# array = [input().split() for i in range(n)]
#
#
# newArray = []
#
# for i in range(m):
#     count = 0
#     for j in range(n):
#         if array[j][i] == "1":
#             count += 1
#     newArray.append(count)
# print(newArray)
# answer = 0
# for i in range(1, len(newArray)):
#     answer += 1
#     if newArray[i-1] - newArray[i] > k:
#         flag = False
#         break
#
# if flag:
#     print("YES")
#     print(n)
# else:
#     print("NO")
#     print(answer)


# 4 Супербутерброд
# print("Супербутерброд")
#
# # Проверяем високосный ли год
# year = int(input())
# if year % 4 == 0 or (year % 100 == 0 and year % 400):
#     print("Високосный год")
#
# day = int(input('Номер дня в году: '))
#
# week = (day - 1) // 7 + 1
# day_of_week = (day - 1) % 7 + 1
#
# print('Номер недели:', week)  # Как указать если первый день не первый элемент в недели
# print('Номер дня в неделе:', day_of_week)


# Слово
# print("Слово")
#
# def fib(line):
#     a = 1
#     b = 1
#     arrayFib = []
#     arrayFib.append(a)
#     for i in range(len(line)):
#       a, b = b, a + b
#       if b <= len(line):
#         arrayFib.append(b)
#     return arrayFib
#
# line = input()
# index = fib(line)
# # print(line[index[0]-1])
# len_line = len(line)
# i = 0
# answer_line = ""
# for i in index:
#     word = line[i-1]
#     answer_line += word
#
# print(answer_line)

# while len_line > 0:
#     word = line[index[i]-1]
#     answer_line += word
#     i += 1
#     len_line -= 1


# Лентяй
# print("Лентяй")
#
# count_subject = int(input())
# min_day = 0
# max_day = 99
# day_start, day_stop = map(int, input().split())
# day_ok = set(range(day_start, day_stop+1))
#
# for i in range(count_subject-1):
#     day_start, day_stop = map(int, input().split())
#     day_two_ok = set(range(day_start, day_stop+1))
#     day_ok &= day_two_ok
#
# if not day_ok:
#     print("NO")
# else:
#     print("YES")


# if day_ok.isdisjoint(day_two_ok):
#     flag = False
# if day_start in day_ok or day_stop in day_ok:
#     pass
# else:
#     flag = False


# if min_day == day_start:
#     pass
# elif min_day < day_start:
#     min_day = day_start
# elif day_stop == max_day:
#     pass
# elif max_day > day_stop:
#     max_day = day_stop
# else:
#     flag = False


# Карусель

# count_tasks = int(input())
# line = input().split()
# ball = 3
# count_ball = 0
# for i in line:
#     i = int(i)
#     if i == 1:
#         count_ball += ball
#         ball += 1
#     if i == 0:
#         ball -= 3
#         if ball < 3:
#             ball = 3
#
# print(count_ball)

# number = int(input())
# # 4 гола = 4 + 3 + 2 + 1
#
# goal = 1
# while number != 0:
#     number -= goal
#     goal += 1
#
# print(goal-1)

# Таблица умножения

# x, y = map(int, input().split())
#
# table = []
# for i in range(x):
#     for j in range(y):
#         table.append(i*j)
#
# for i in range(len(table)):
#     for


# # Обновлённая проверка даты
# from datetime import datetime
# from calendar import monthrange
#
# current_year = datetime.now().year
# month_now = datetime.now().month
#
#
# # yesterday = 1 #datetime.now().day # Тест
# yesterday = datetime.now().day
# day_start = yesterday - 3
# day_end = yesterday + 4
#
# days_in_month_before = monthrange(current_year, month_now)[1]
# days_in_month = monthrange(current_year, month_now)[1]
# days_in_next_month = monthrange(current_year, month_now+1)[1]
# print(days_in_month)
# days_in_month_before_array = [element for element in range(1, days_in_month_before + 1)]
# days_in_month_array = [element for element in range(1, days_in_month+1)]
# days_in_next_month_array = [element for element in range(1, days_in_next_month+1)]
#
# max_day = max(days_in_month_array)
#
#
# our_days = []
# for i in range(day_start, day_end):
#     if i in days_in_month_array:
#         our_days.append(i)
#     elif i > max_day:
#         our_days.append(i-days_in_month_array[-1])
#     else:
#         # days_in_month_before_array.reverse()
#         our_days.append(days_in_month_before_array[i-1])
#
# print()
# print(our_days)
# print()

# TODO 276 68, 577, 706, 511

# # Разбиение на части
# print("Разбиение на части")
#
# n, m = map(int, input().split())
# answer = [n//m]*(m-(n % m))
#
# answer2 = [n//m+1] * (n % m)
# # print(answer2)
# print(*(answer+answer2))


# 68 Дом - Школа - Дом
# print("Дом - Школа - Дом")
# location = input()
# travel = int(input())
#
# # our_location = {"School"}
# if location == "School" and travel % 2 == 0:
#     print("No")
# else:
#     print("Yes")

# 577 Таблица умножения

# n, m = map(int, input().split())
#
# multiplication_table = [0]*10
# # print(multiplication_table)
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         result = i*j
#         while result > 0:
#             multiplication_table[result % 10] += 1
#             result //= 10
#         # for digit in str(result):
#         #     digit = int(digit)
#         #     multiplication_table[digit] += 1
# # print(*multiplication_table)
# for i in multiplication_table:
#     print(i)


# count_digit = dict.fromkeys(range(10), 0)

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         result = i*j
#         for digit in str(result):
#             digit = int(digit)
#             count_digit[digit] = count_digit.get(digit, 0) + 1
#
# for key in count_digit:
#     print(count_digit[key])


# for number in multiplication_table:
#     number = str(number)
#     for digit in number:
#         digit = int(digit)
#         count_digit[digit] = count_digit.get(digit, 0)+1

# print(count_digit)
# for key in count_digit:
#     print(count_digit[key])


# TODO 706 511 331 131 691 43

# 706 ?

# r, x, y = map(float, input().split())
#
# l = abs(x) * r / (2 * r - y)
# print(l)

# 511  Wrong answer 51 тест
# print(511)
#
# # he_is_in_line = int(input())
# for he_is_in_line in range(1, 200):
#     print(he_is_in_line, end=" ")
#     front_of_him = he_is_in_line - 1
#     all_minute = front_of_him * 5
#     hours = all_minute // 60
#     minute = all_minute % 60
#     if he_is_in_line >= 146:
#         print("NO")
#     else:
#         print(int(hours), int(minute))

# 331 не смог найти как правильно отформатировать
# print(331)
# print(70 % 60)
# print(70//60)
# start_h, start_m = map(int, input().split(":"))
#
# h, m = map(int, input().split())
# answer_m = (start_m + m) % 60
# plus_h = (start_m + m) // 60
# answer_h = (start_h + h + plus_h) % 24
# print("{:02d}:{:02d}".format(answer_h, answer_m))


# 131 Accepted
# print(131)
#
# a = int(input())
# max_year = 0
# answer = -1
# for i in range(a):
#     year, gender = map(int, input().split())
#     if gender == 1:
#         if max_year < year:
#             max_year = year
#             answer = i+1
# print(answer)


# 691
# print(691)
#
# import re
# a = int(input())
# answer = r"^[ABCEHKMOPTXY]\d{3}[ABCEHKMOPTXY]{2}$"
# for i in range(a):
#     line = input()
#     if re.search(answer, line):
#         print("Yes")
#     else:
#         print("No")


# 43
# import re
#
# line = input()
# zero = re.findall("0+", line)
# if len(zero) == 0:
#     print(0)
# else:
#     print(len(max(zero)))

# 283
# test = ["ava", "ascd"]
# count = 0
# for i in test:
#     count += len(i)
# print(count)
# import re
#
# line = input()
# check = r"([A-Z][a-z]{1,3})+"
# if re.match(check, line):
#     print("Yes")
# else:
#     print("No")
# reg_arr = re.findall(check, line)
# # print(reg_arr)
# count = 0
# for i in reg_arr:
#     count += len(i)
# if len(line) == count:
#     print("Yes")
# else:
#     print("No")

# №641
# print("Странная лотерея")
#
# array = list(input())
# start_array = array.copy()
#
# max_number = 0
# for i in range(len(array)):
#     for j in range(i+1, len(array)):
#         var = array[:i]
#         var2 = array[i+1:j]
#         var3 = array[j+1:]
#         # print(var, var2, var3)
#         # print(i, j)
#         array = var + var2 + var3
#         array = int("".join(array))
#         if max_number < array:
#             max_number = array
#             # print(array)
#         array = start_array
# print(max_number)

# max_number = 0
# for i in range(len(array)):
#     for j in range(i, len(array)):
#
#         var = array[:i]
#         var2 = array[i + 1:j]
#         var3 = array[j + 1:]
#         array =
#         if max_number < int(array[0]):
#             max_number = int(array[0])
#         array = start_array
# print(max_number)

# 93
# print("Боги")
#
# corrective_god_iterable = int(input())
# corrective_god = []
# for _ in range(corrective_god_iterable):
#     corrective_god.append(input())
#
# check_god_iterable = int(input())
# check_god = []
# for _ in range(check_god_iterable):
#     check_god.append(input())
#
#
# def check_word(word, word2):
#     if len(word) == len(word2):
#         count = 0
#         for i in range(len(word)):
#             if word[i] != word2[i]:
#                 count += 1
#         if count == 1:
#             return True
#
# array_count = []
# for i in range(corrective_god_iterable):
#     count = 0
#     for j in range(check_god_iterable):
#         if check_word(corrective_god[i], check_god[j]):
#             count += 1
#     array_count.append(count)
# print(*array_count)

# array_count = []
# for i in range(corrective_god_iterable):
#     max_count = 0
#     for j in range(check_god_iterable):
#         if len(corrective_god[i]) == len(check_god[j]):
#             count = len(set(corrective_god[i]).intersection(corrective_god[j]))
#             if len(corrective_god)-1 == count:
#                 max_count += 1
#         array_count.append(max_count)
# print(*array_count)

# TODO 574, 13, 287, 164
# 574
# print("Анаграммы")
# line = list(input())
# line2 = list(input())
#
# index = len(line)-1
# index2 = len(line2)-1
# for i in range(len(line)):
#     for j in range(len(line2)):
#         if line[index] == line2[index2]:
#             print(index, index2)
#             print(line.pop(index))
#             print(line2.pop(index2))
#             print(line)
#             print(line2)
#             index -= 1
#             index2 -= 1
#         index2 -= 1
#         print(index, index2)
#     index -= 1
# print(line, line2)
# print(line[i])
# print(line.remove(line[i])) # Почему ошибочка

# line = list(input())
# line2 = list(input())
#
# line_dict = {}
# line_dict2 = {}
#
# for i in range(len(line)):
#     line_dict[line[i]] = line_dict.get(line[i], 0) + 1
#
# for i in range(len(line2)):
#     line_dict2[line2[i]] = line_dict2.get(line2[i], 0) + 1
#
# if line_dict == line_dict2:
#     print("YES")
# else:
#     print("NO")

# 13
# Циклом пробегаться проверять на одинаковых ли позициях стоят, если да, то быки += 1
# если равны но не по позиции то += коровы и удаляем оба элемента из массивов, только вот как правильно бежать по массивам)

# line, line2 = list(map(str, input().split()))
#
# array = [False, False, False, False]
# bulls = 0
# cows = 0
# for i in range(len(array)):
#     if line[i] == line2[i] and array[i] == False:
#         bulls += 1
#         array[i] = True
# for i in range(len(array)):
#     for j in range(len(array)):
#         if line[i] == line2[j] and array[i] == False:
#             cows += 1
#             array[i] = True
#
# print(bulls, cows)

# line_dict = dict()
# line2_dict = dict()

# for i in range(len(line)):
#     line_dict[line[i]] = False
#     line2_dict[line2[i]] = False
#
# for key, value in line_dict.items():
# 287
# n, m = map(int, input().split())
# line = input()
# set_line = set()
#
# for i in range(m, len(line)+1):
#     set_line.add(line[i-m:i])
#
# print(len(set_line))

# TODO 164 не получилось, 17 тест - ошибка

# print("Счастливый билет")
#
# line = input()
# len_line = len(line)
#
#
# # print(first_half, second_half)
#
# def total_sqr(number):
#     total = sum(map(int, number))
#
#     while total >= 10:
#         total = sum(map(int, str(total)))
#     return total
#
#
# for i in range(1, len(line)):
#     first_since = line[:i]
#     second_since = line[i:]
#     total = total_sqr(first_since)
#     total2 = total_sqr(second_since)
#     if total == total2:
#         print("YES")
#         break
# else:
#     print("NO")

# TODO 163, 168, 847

# 163
# print("Уравнение для 5 класса!")
#
# line = input()
# number1 = line[0]
# sign = line[1]
# number2 = line[2]
# answer = line[-1]
# unknown = 0
# if sign == "+":
#     if number1.isdigit() and answer.isdigit():
#         number2 = int(answer) - int(number1)
#         unknown = number2
#     elif number2.isdigit() and answer.isdigit():
#         number1 = int(answer) - int(number2)
#         unknown = number1
#     else:
#         answer = int(number1) + int(number2)
#         unknown = answer
# elif sign == '-':
#     if number1.isdigit() and answer.isdigit():
#         unknown = int(number1) - int(answer)
#     elif number2.isdigit() and answer.isdigit():
#         unknown = int(number2) + int(answer)
#     else:
#         unknown = int(number1) - int(number2)
# print(unknown)
#
#
# # TODO 168 доделать - не очень понял)

# 847 test 10 - ошибка

# flag = True
# word, word2 = map(str, input().split())
#
# word_dict = {}
# word_dict2 = {}
#
# if set(word).intersection(set(word2)) and len(word) == len(word2):
#     for i in range(len(word)):
#         word_dict[word[i]] = word_dict.get(word[i], 0) + 1
#
#     for i in range(len(word2)):
#         word_dict2[word2[i]] = word_dict2.get(word2[i], 0) + 1
#
#
#     if word_dict == word_dict2:
#         for i in range(len(word)):
#             if word[i] == word2[i]:
#                 print("NO")
#                 flag = False
#                 break
#         if flag:
#             print("YES")
#     else:
#         print("NO")
#
# else:
#     print("NO")


# if word.intersection(word2):
#     print("YES")
# else:
#     print("NO")


# 28
# with open('26data (1)/26-J3.txt') as f:
#     s, n = map(int, f.readline().split())
#     numbers = [int(x) for x in f]
#
#     numbers_sort = sorted(numbers, reverse=True)
#     answer_array = []
#     for i in range(len(numbers_sort)):
#         if s >= numbers_sort[i]:
#             s -= numbers_sort[i]
#             answer_array.append(numbers_sort[i])
# print(len(answer_array), answer_array[-1])

# 31
# test_array = [1, 4, 7, 8]
# new_test_array = test_array[-1: -3: -1]
# print(new_test_array)

# n = int(input())
#
# all_purchases = []
# for _ in range(n):
#     price = int(input())
#     all_purchases.append(price)
#
# all_purchases = sorted(all_purchases, reverse=True)
# index = 0
# for i in range(len(all_purchases)):
#     if all_purchases[i] < 101:
#         index = i
#         break
# print(f"all_purchases: {all_purchases}")
# print(f"index: {index}")
# discounted_products = all_purchases[:index]
# print(f"discounted_products: {discounted_products}")
# count_discounted_products = len(discounted_products)//2
# print(f"count_discounted_products: {discounted_products}")
#
# # apply_discount = discounted_products[-1: -count_discounted_products-1: -1]
# apply_discount = discounted_products[count_discounted_products+1:]
# print(f"apply_discount: {apply_discount}")
# max_discount_product = max(apply_discount)
# print(f"max_discount_product: {max_discount_product}")
# new_apply_discount = []
# for i in range(len(apply_discount)):
#     discount = apply_discount[i]/100*10
#     price = apply_discount[i]
#     new_price = price - discount
#     # print(f"price: {price} discount: {discount} new_price: {new_price}")
#     apply_discount[i] = new_price
#
# j = 0
# print(f"index-count_discounted_products: {index-count_discounted_products}, index: {index}")
# for i in range(index-count_discounted_products, index):
#     # discount = apply_discount[j]/100*10
#     # price = apply_discount[j]
#     # new_price = price - discount
#     # print(f"price: {price} discount: {discount} new_price: {new_price}")
#     # all_purchases[i] = new_price
#     all_purchases[i] = apply_discount[j]
#     j += 1
#
# print(all_purchases)
# total = round(sum(all_purchases))
# print(total, max_discount_product)


# 34
# print(34)
# import math
#
# count_file = int(input())
#
# files = []
# for _ in range(count_file):
#     files.append(int(input()))
#
# total_storage = sum(files)
# available = total_storage // 10  # ам нужно столько сэкономить
# print(f"total: {total_storage}, available: {available}")
# # need_to_save = total_storage-available
# files = sorted(files, reverse=True)
# print(files)
#
# total_saved_space = 0
# index = 0
# new_files = []
# for i in range(len(files)):
#     saved_space = (files[i] * 0.2)
#     print(f"saved_space: {saved_space}")
#     after_compression = files[i] - saved_space
#     # files[i] = after_compression
#     new_files.append(after_compression)
#     total_saved_space += saved_space
#     if total_saved_space >= available:
#         index = i
#         break
#
# # number_of_uncompressed_files = len(files[index+1:])
# number_of_uncompressed_files = len(files) - len(new_files)
# largest_uncompressed_file = files[index]
# print(number_of_uncompressed_files, largest_uncompressed_file)

# 35
# print(35)
# peoples = int(input())
#
# money_peoples = []
# for i in range(peoples):
#     money_peoples.append(int(input()))
#
# total_contribution = sum(money_peoples)*0.6
#
# sorted_money_peoples = sorted(money_peoples, reverse=True)
# print(sorted_money_peoples)
#
# count_rich_peoples = int(len(sorted_money_peoples) * 0.2)
# count_other_peoples = len(sorted_money_peoples) - count_rich_peoples
# rich_peoples = sorted_money_peoples[:count_rich_peoples]
# print(rich_peoples)
#
# total_contribution_rich = 0
# for i in range(len(rich_peoples)):
#     total_contribution_rich += rich_peoples[i] * 0.8
#
# left_contribution = total_contribution - total_contribution_rich
# print(f"left_contribution: {left_contribution}")
#
# money_other_peoples = sum(sorted_money_peoples[count_rich_peoples:])
# percent_for_others = left_contribution/money_other_peoples
# print(f"percent_for_others: {percent_for_others}")
#
# small_contribution = sorted_money_peoples[-1] * percent_for_others
#
# print(int(total_contribution_rich), int(small_contribution))


# TODO
# number_of_goods = int(input())
# commodity_prices = list(map(int, input().split()))
# print(commodity_prices)
# # for i in range(number_of_goods):
# #     commodity_prices.append(int(input()))
#
# first_stock = int(len(commodity_prices) * 0.7)
# new_price_one = []
# for i in range(first_stock):
#     new_price_one.append(commodity_prices[i]*0.3)
# for i in range(first_stock, len(commodity_prices)):
#     new_price_one.append(commodity_prices[i]*0.4)
#
# total_new_price_one = sum(new_price_one)
#
# second_stock = int(len(commodity_prices) * 0.5)
# new_price_two = []
# for i in range(second_stock):
#     new_price_two.append(commodity_prices[i]*0.4)
#
# for i in range(second_stock, len(commodity_prices)):
#     new_price_two.append(commodity_prices[i]*0.35)
#
# total_new_price_two = sum(new_price_two)
#
# if total_new_price_one > total_new_price_two:
#     print(total_new_price_one-total_new_price_two, new_price_one[0])
# else:
#     print(total_new_price_two-total_new_price_one, new_price_two[0])

# 37, 39

# 37

# total_packages, packages_to_send = map(int, input().split())
#
# array_package = []
#
# for i in range(total_packages):
#     weight_and_price_array = []
#     weight, price = map(int, input().split())
#     weight_and_price_array.append(weight)
#     weight_and_price_array.append(price)
#     array_package.append(weight_and_price_array)
#
# array_package = sorted(array_package, reverse=True)
# print(array_package)
#
# array_weight = []
# array_price = []
# for i in range(packages_to_send):
#     array_weight.append(array_package[i][0])
#     array_price.append(array_package[i][1])
#
# print(array_weight)
# print(array_price)
#
# print(sum(array_weight), array_price[0])  # У меня получилось 271 910, должно 261 910


# 39

quantity_of_cargo, truck_capacity = map(int, input().split())

mass_of_goods_array = []

for i in range(quantity_of_cargo):
    mass_of_goods_array.append(int(input()))

mass_of_goods_array = sorted(mass_of_goods_array, reverse=True)




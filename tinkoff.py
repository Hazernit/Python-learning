# TODO 1.1
# a, b, c, d = map(int, input().split())
#
# pereplata = d - b
#
# money_pereplata = pereplata * c
#
# result = a + money_pereplata
#
# if result < a:
#     result = a
# print(result)

# Второй вариант 1.2

# if d > b:
#     difference_mb = d - b
#
#     difference_money = difference_mb * c
#
#     result = difference_money + a
# else:
#     result = a
# print(result)

# TODO 2.1
# import math
#
# a = int(input())
# print(math.ceil(a/2))

# # TODO 3.1
#
# people, time_min = map(int, input().split())
# floor = list(map(int, input().split()))  # этаж
# index_min_time = int(input())-1
#
# total_time = 0
#
# time_floor = floor[index_min_time]
# # print(time_floor, time_floor < time_min)
# right_time = 0
#
# for i in range(index_min_time+1, len(floor)):
#     # print(floor[i], end=" ")
#     next_floor = floor[i]
#     current = floor[i-1]
#     distance = next_floor - current
#     right_time += distance
#
# if time_floor <= time_min:
#     for i in range(1, len(floor)):
#         distance = floor[i] - floor[i-1]
#         total_time += distance
# elif right_time <= time_min:
#     for i in range((len(floor))-1, 0, -1):
#         # print(floor[i-1], floor[i])
#         distance = floor[i] - floor[i-1]
#         # print(distance)
#         total_time += distance
#         # print(floor[i], end=" ")
# else:
#     right = 0
#     # print("right")
#     for i in range(index_min_time+1, len(floor)):
#         distance = floor[i] - floor[i-1]
#         # print(f"floor[i]: {floor[i]}, floor[i-1]: {floor[i-1]}")
#         right += distance
#     left = 0
#     # print("left")
#     for i in range(1, index_min_time+1):
#         distance = floor[i] - floor[i-1]
#         # print(f"floor[i]: {floor[i]}, floor[i-1]: {floor[i - 1]}")
#         left += distance
#     # print(right, left)
#     if left < right:
#         total_time = left * 2 + right
#     else:
#         total_time = right * 2 + left
# print(total_time)


# a = int(input())
#
# b = 0
# answer = 0
#
# while answer < a:
#     b += 1
#     answer = 2**b
#
# print(b)


# n, t = map(int, input().split())
# floor = list(map(int, input().split()))  # этаж
# index_min_time = int(input())-1
#
# s = 0  # время
#
# for i in range(1, n):
#     s += floor[i] - floor[i-1]
#     if i == index_min_time:
#         if s > t:
#             s = float("inf")
#             break
# print("первый цикл s = ", s)
# min_s = s
#
# s = 0  # время
#
# for i in range(n-1, -1, -1):
#     s += floor[i] - floor[i-1]
#     if i == index_min_time:
#         if s > t:
#             s = float("inf")
#             break
# print("второй цикл s = ", s)
# min_s = min(s, min_s)
#
# for i in range(1, n-1):
#     s = 0
#     for j in range(i+1, n):
#         s += floor[j] - floor[j-1]
#         if j == index_min_time:
#             if s > t:
#                 s = float("inf")
#                 break
#     for j in range(n-2, -1, -1):
#         s += floor[j] - floor[j-1]
#         if j == index_min_time:
#             if s > t:
#                 s = float("inf")
#                 break
# print("третий цикл s = ", s)
#
# min_s = min(min_s, s)
#
# flag = False
# for i in range(1, n-1):
#     s = 0
#     for j in range(i, 0, -1):
#         print(floor[j], floor[j-1])
#         s += floor[j] - floor[j-1]
#         if j == index_min_time:
#             flag = True
#             if s > t:
#                 s = float("inf")
#                 break
#         if flag and s != "inf":
#             new_start = j
#     for j in range(n):
#         s += floor[j] - floor[j-1]
#         if j == index_min_time:
#             if s > t:
#                 s = float("inf")
#                 break
# print("четвёртый цикл s = ", s)
# min_s = min(s, min_s)
# print(min_s)


# a = int(input())
#
# b = 0
# answer = 0
#
# if a == 1:
#  print(0)
# else:
#     while answer < a:
#         b += 1
#         answer = 2 ** b
#
#     print(b)


# n, t_w = map(int, input().split())
# floors = list(map(int, input().split()))
# i_w = int(input()) - 1
#
#
# def f(t, i):
#     was_t = False
#     if i == i_w:
#         was_t = True
#         if t > t_w:
#             t = float('inf')
#
#     return was_t, t
#
#
# # От первого слева направо
# t = 0
# for i in range(1, n):
#     t += floors[i] - floors[i - 1]
#     was_t, t = f(t, i)
#
# min_t = t
#
# # От последнего справа налево
# t = 0
# for i in range(n - 1, 0, -1):
#     t += floors[i] - floors[i - 1]
#     was_t, t = f(t, i)
#
# min_t = min(t, min_t)
#
# # Для каждого работника, кроме первого и последнего
# for i in range(1, n - 1):
#     t = 0
#     was_t = False
#     for j in range(i + 1, n):
#         t += floors[j] - floors[j - 1]
#         was_tt, t = f(t, j)
#         was_t = was_t or was_tt
#
#     for j in range(n - 1, 0, -1):
#         t += floors[j] - floors[j - 1]
#         if not was_t:
#             was_tt, t = f(t, j)
#             was_t = was_t or was_tt
#
#     min_t = min(min_t, t)
#
#     t = 0
#     was_t = False
#     for j in range(i, 0, -1):
#         t += floors[j] - floors[j - 1]
#         was_tt, t = f(t, j)
#         was_t = was_t or was_tt
#
#     for j in range(1, n):
#         t += floors[j] - floors[j - 1]
#         if not was_t:
#             was_tt, t = f(t, j)
#             was_t = was_t or was_tt
#
#     min_t = min(min_t, t)
#
# print(min_t)

# 4

# n, k = map(int, input().split())
# array = list(map(int, input().split()))
#
# array.sort(key=lambda x: (-len(str(x)), x))
#
# print(array)
#
# total_before = sum(array)
#
# for i in range(k):
#     before_digit = array[i]
#     before_digit = str(before_digit)
#     find_nine = before_digit.find("9")
#     if find_nine == 0:
#         before_digit = before_digit[1:]
#     print(before_digit)

# a = len(str(array[i]))
# print("a =", a)
# find_digit = ((int(a)-1)*10)
# print("find_digit =", find_digit)
# digit = array[i] // find_digit
# print("digit", digit)
# new_digit = str(digit) + str(before_digit % find_digit)
#
# print(new_digit)


# total_after = sum(array)
#
# result = total_after - total_before
# print(result)

# TODO адаптировать под задачу
from random import randint

# numbers = [randint(1, 9) for _ in range(10)]
# numbers.extend(randint(10, 99) for _ in range(10))
# numbers.extend(randint(100, 999) for _ in range(10))
#
# print(numbers)

# numbers = [8, 78, 0, 95,  98, 3, 7, 10, 23, 23, 5, 1, 2, 1, 3, 5]
# numbers = [1, 2, 1, 3, 5, 98, 333, 789]
# print(len(numbers))

# Задание
# n, k = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# for i in range(len(numbers)):
#     x = str(numbers[i])
#     x = x.lstrip('9')
#     if x == '':
#         x = '0'
#     numbers[i] = x
#
# numbers = [x for x in numbers if x != '0']
#
# numbers.sort(key=lambda x: (-len(str(x)), x))
#
# # print(numbers)
#
# # n_max_ops = 15
# n_max_ops = k
# total = 0
# for i in range(n_max_ops):
#     if not numbers:
#         break
#     old = x = str(numbers[0])
#     dx = (9 - int(x[0])) * 10 ** (len(x) - 1)
#     total += dx
#     x = x[1:]
#     x = x.lstrip('9')
#     if x == '':
#         numbers.pop(0)
#     else:
#         # numbers[0] = int(x)
#         numbers[0] = x
#     # print(old, '->', x, ':', dx)
#
#     numbers.sort(key=lambda x: (-len(str(x)), x))
#
# print(total)


# TODO 5
# l, r = map(int, input().split())

# count = 0

# 50 300000
# digit_is(min_marginal_value) 5
# 100 - 1000 -> 9
# 1000 - 10000 -> 9
# 10000 - 100000 -> 9
# digit_is(max_marginal_value) 2

# numbers = [randint(1, 9) for _ in range(10)]
# numbers.extend(randint(10, 99) for _ in range(10))
# numbers.extend(randint(100, 999) for _ in range(10))

# l, r = map(int, input().split())
# while True:
#     numbers = [randint(1, 10 ** 18) for _ in range(2)]
#     numbers.sort()
#     l, r = numbers
l, r = map(int, input().split())
print(l, r)

a = len(str(l))
b = len(str(r))
print('длина a', a, 'длина b', b)
## count = (len(str(r))-1) - (len(l)+1)  # 100% там 9 значений удовлетворяющих условие
if a != b:
    count = b - a - 1
    result = count * 9
    # print(result)
else:
    result = 0


def digit_is(number):
    s = str(number)
    our_numbers = [str(i) * len(s) for i in range(1, 10)]
    return our_numbers


numbers_for_min_marginal = digit_is(l)
# print(numbers_for_min_marginal)

if a == b:
    min_index = 10
    max_index = 0
    for i in range(len(numbers_for_min_marginal)):
        num = int(numbers_for_min_marginal[i])
        if l <= num and min_index > i:
            min_index = i
        if r >= num and max_index < i:
            max_index = i
    print(max_index, min_index)
    result = max_index - min_index + 1
    print(result)
else:
    min_marginal_value = 0
    for i in range(len(numbers_for_min_marginal)):
        if l <= int(numbers_for_min_marginal[i]):
            print('i', i)
            print('l:', l, 'numbers_for_min_marginal[i]:', numbers_for_min_marginal[i])
            min_marginal_value = len(numbers_for_min_marginal) - i
            print(min_marginal_value)
            break
    ## print(min_marginal_value)
    ## if min_marginal_value is None:
    ##     min_marginal_value = 0
    result += min_marginal_value

    numbers_for_max_marginal = digit_is(r)
    print(numbers_for_max_marginal)
    max_margin_value = 0
    for i in range(len(numbers_for_max_marginal)):
        if r >= int(numbers_for_max_marginal[i]):
            print('i', i)
            print('r:', r, 'numbers_for_max_marginal[i]:', numbers_for_max_marginal[i])

            max_margin_value += 1
            print(max_margin_value)
    if max_margin_value is None:
        max_margin_value = 0
    print(max_margin_value)
    result += max_margin_value
print(result)


# for i in range(l, r+1):
#     if len(str(i)) == 1:
#         count += 1
#     elif len(str(i)) == 2 and i % 11 == 0:
#         count += 1
#     elif len(str(i)) == 3 and i % 111 == 0:
#         count += 1
#     elif len(str(i)) == 4 and i % 1111 == 0:
#         count += 1
#     elif len(str(i)) == 5 and i % 11111 == 0:
#         count += 1
#     elif len(str(i)) == 6 and i % 111111 == 0:
#         count += 1
#     elif len(str(i)) == 7 and i % 1111111 == 0:
#         count += 1
#     elif len(str(i)) == 8 and i % 11111111 == 0:
#         count += 1
#     elif len(str(i)) == 9 and i % 111111111 == 0:
#         count += 1
#     elif len(str(i)) == 10 and i % 1111111111 == 0:
#         count += 1
#     elif len(str(i)) == 11 and i % 11111111111 == 0:
#         count += 1
#     elif len(str(i)) == 12 and i % 111111111111 == 0:
#         count += 1
#     elif len(str(i)) == 13 and i % 1111111111111 == 0:
#         count += 1
#     elif len(str(i)) == 14 and i % 11111111111111 == 0:
#         count += 1
#     elif len(str(i)) == 15 and i % 111111111111111 == 0:
#         count += 1
#     elif len(str(i)) == 16 and i % 1111111111111111 == 0:
#         count += 1
#     elif len(str(i)) == 17 and i % 11111111111111111 == 0:
#         count += 1
#     elif len(str(i)) == 18 and i % 111111111111111111 == 0:
#         count += 1

# print(count)

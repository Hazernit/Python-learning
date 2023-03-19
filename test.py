# from music.classiccal.composers import of_the_18th_century
# from . import my_module

# print("Test")
# x1, y1 = 0, 0
# x2, y2 = map(int, input().split())
#
# d = ((x1-x2)**2 + (y1-y2)**2)
# d_exact = ((x1-x2)**2 + (y1-y2)**2)**0.5
# print(f"√{d}")
# print(d_exact)
# import my_module
#
# my_module.printer(my_module.name)

# with open('egor.txt') as f:
#     text = f.read()
#     our_set = {" "}
#     text_set = set(text)
#     print(text_set)
#     print(len(text_set))
#
#     text_set.discard(" ")
#     # text_set.difference_update(our_set)
#
#     print(text_set)
#     print(len(text_set))


# text_set = set(text)
# print(text_set)
# unique = list(set(text))
#
#
# print("Количество уникальных символов: ", unique)
# print (len(unique))


# L = [int(input()) % 2 == 0 for i in range(5)]
# print(any(L))

# def divisibility():
#     print("Привет")
# return n % a == 0
# if n % a == 0:
#     return True
# else:
#     return False

# a = int(input())
# b = int(input())


# print("Работаем")
# def ladder(number):
#     symbol = "*"
#     total_symbol = ""
#     while number > 0:
#         for _ in range(number):
#             total_symbol += symbol
#         print(total_symbol)
#         total_symbol = ""
#         number -= 1
#
# ladder(6)

# 8, 78, 95
# 8, 78, 5
# print('95'.lstrip('9'))
#
# numbers = [8, 78, 0, 95, 0]
# numbers = [x for x in numbers if x != 0]
#
# print(numbers)

# numbers = [8, 78, 0, 95,  98, 3, 7, 10, 23, 23, 5, 1, 2, 1, 3, 5]
# numbers = [1, 2, 1, 3, 5]
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
print(len(numbers))

for i in range(len(numbers)):
    x = str(numbers[i])
    x = x.lstrip('9')
    if x == '':
        x = '0'
    numbers[i] = int(x)

numbers = [x for x in numbers if x != 0]

numbers.sort(key=lambda x: (-len(str(x)), x))

print(numbers)

n_max_ops = k
# for i in numbers:
#     i = str(i)
#     n_max_ops += len(i)

total = 0
for i in range(n_max_ops):
    if not numbers:
        break
    old = x = str(numbers[0])
    print(f"(9 - {int(x[0])}) * 10 ** {len(x) - 1}")
    result = (9 - int(x[0])) * 10 ** (len(x) - 1)
    print(f"{(9 - int(x[0]))} * 10 ** {len(x) - 1} = {result}")
    dx = (9 - int(x[0])) * 10 ** (len(x) - 1)
    total += dx
    x = x[1:]
    x = x.lstrip('9')
    if x == '':
        numbers.pop(0)
    else:
        numbers[0] = x

    print(old, '->', x, ':', dx)

    numbers.sort(key=lambda x: (-len(str(x)), x))

print(total)


# print("test")
# array = [1, 23, 34, 7]
#
# n_max_ops = 0
# for i in array:
#     i = str(i)
#     n_max_ops += len(i)
#
# print(n_max_ops)


































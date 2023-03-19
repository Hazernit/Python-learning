def numbers(x):
    return [str(i) * len(x) for i in range(1, 10)]


l, r = input().split()

count = 0

for ln in range(len(l) + 1, len(r)):
    count += 9

if len(l) != len(r):
    nums = numbers(l)

    for num in nums:
        if l <= num:
            # print(num)
            count += 1

    nums = numbers(r)

    for num in nums:
        if num <= r:
            count += 1

else:
    nums = numbers(l)

    for num in nums:
        if l <= num <= r:
            count += 1

print(count)


# Генерируем нужные числа
def numbers(x):
    return [str(i) * len(x) for i in range(1, 10)]


l, r = input().split()

count = 0

# Мы учитываем все числа, длинной больше l и меньше r
for ln in range(len(l) + 1, len(r)):
    print('Учли_1', numbers('1' * ln))
    count += 9


if len(l) != len(r):
    nums = numbers(l)

    # Сгенерировали все числа длиной l
    # И выбираем подходящие
    for num in nums:
        if l <= num:
            print('Учли_2', num)
            count += 1

    nums = numbers(r)

    # Сгенерировали все числа длиной r
    # И выбираем подходящие
    for num in nums:
        if num <= r:
            print('Учли_3', num)
            count += 1

else:
    nums = numbers(l)
    # Если длины одинаковые, то создаём только один массив и выбираем нужные
    for num in nums:
        if l <= num <= r:
            print('Учли_4', num)
            count += 1

print(count)
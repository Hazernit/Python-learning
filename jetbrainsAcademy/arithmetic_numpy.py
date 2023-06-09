import numpy as np

list_a = [1, 2, 3, 4]
array_a = np.array(list_a)

list_b = [11, 22, 33, 44]
array_b = np.array(list_b)

print(array_a + array_b)  # Сумма двух массивов (мы не можем складывать массивы разной длинны)

print(list_a + list_b)  # Однако применительно к спискам сложение просто объединяет их вместе

# Точно так же, если мы попытаемся умножить список на n,
# мы получим список, повторенный n раз,
# в то время как с массивом каждый элемент будет умножен на n :
print(list_a * 3)   # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(array_a * 3)  # [3 6 9 12]


first = np.array([1, 2, 3, 4, 5])
second = np.array([[1, 1, 1],
                   [2, 2, 2]])

# Чтобы узнать размер измерения, используйте shape.
# Первое число вывода указывает количество строк,
# а второе — количество столбцов.
print(second.shape)  # (2, 3)


# Если массив NumPy имеет только одно измерение, результат будет немного другим:
# В этом случае первое число — это не количество строк,
# а количество элементов в единственном измерении,
# а пустое место после запятой означает, что второго измерения нет.

print(first.shape)   # (5,)


# Длина shape кортежа - это количество осей, ndim.

print(first.ndim)   # 1
print(second.ndim)  # 2


# Функция len()возвращает длину массива и size
# дает нам количество элементов в массиве.

print(len(first), first.size)    # 5 5
print(len(second), second.size)  # 2 6

# Обратите внимание, что в первом случае они возвращают одно и то же значение,
# а во втором случае числа различаются. Дело в том, len()что он работает так же,
# как и с обычными списками, поэтому,
# если мы рассматриваем двумерный массив выше как список,
# содержащий два вложенных списка, становится ясно,
# что для нахождения его длины учитываются только вложенные списки.
# Size, напротив, учитывает каждый отдельный элемент во всех вложенных списках.
#
# Еще одна вещь, на которую следует обратить внимание, это то,
# что и длину, и размер массива также можно определить по его форме:
# длина — это фактически длина первого измерения, поэтому она равна shape[0],
# а размер — это общее количество элементов,
# равное произведение всех элементов фигурного кортежа.

test_array = np.zeros((3, 2, 6, 1))
print("test_array")

print(test_array.ndim)
print(test_array.size)
print(len(test_array))
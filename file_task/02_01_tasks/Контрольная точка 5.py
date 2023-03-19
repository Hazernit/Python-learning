# Скопируйте код заготовки программы в ячейку.
#
# apple_box_weight =
# n_apple_boxes =
# print('Каждый ящик с яблоками весит', apple_box_weight, 'кг.')
# print('Всего', n_apple_boxes, 'ящиков')
#
# banana_box_weight =
# n_banana_boxes =
# print('Каждый ящик с бананами весит', banana_box_weight, 'кг.')
# print('Всего', n_banana_boxes, 'ящиков')
#
# full_apple_weight =
# print('Общий вес ящиков с яблоками:', full_apple_weight)
#
# full_banana_weight =
# print('Общий вес ящиков с бананами:', full_banana_weight)
#
# full_weight =
# print('Общий вес всех ящиков:', full_weight)
# Ваша задача состоит в том, чтобы дополнить каждую команду присваивания выражением (справа от =).
# Выражения должны быть такими, чтобы при запуске программы вывод на экран был следующим:
#
# Каждый ящик с яблоками весит 15 кг.
# Всего 5 ящиков
# Каждый ящик с бананами весит 20 кг.
# Всего 7 ящиков
# Общий вес ящиков с яблоками: 75
# Общий вес ящиков с бананами: 140
# Общий вес всех ящиков: 215
# Одно число тоже считается выражением.
#
# Программа должна давать корректные результаты при изменении количества ящиков и их веса.
# Например, при изменении веса ящика с бананами с 20 кг до 30 кг общий вес ящиков с бананами должен увеличиться до 210 кг, а вес всех ящиков - до 285 кг.

apple_box_weight = 15
n_apple_boxes = 5
print('Каждый ящик с яблоками весит', apple_box_weight, 'кг.')
print('Всего', n_apple_boxes, 'ящиков')

banana_box_weight = 20
n_banana_boxes = 7
print('Каждый ящик с бананами весит', banana_box_weight, 'кг.')
print('Всего', n_banana_boxes, 'ящиков')

full_apple_weight = apple_box_weight * n_apple_boxes
print('Общий вес ящиков с яблоками:', full_apple_weight)

full_banana_weight = banana_box_weight * n_banana_boxes
print('Общий вес ящиков с бананами:', full_banana_weight)

full_weight = full_apple_weight + full_banana_weight
print('Общий вес всех ящиков:', full_weight)


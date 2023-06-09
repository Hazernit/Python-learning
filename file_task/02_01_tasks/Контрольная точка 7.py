# Контрольная точка 7
# Скорость, время и расстояние
# Пройденное автомобилем расстояние distance рассчитывается как произведение средней скорости его движения speed на время движения time. Напишите программу, которая требует ввода speed и time с клавиатуры и выводит информацию о distance на экран.
#
# Образец работы программы:
#
# Скорость движения (км/ч): 80
# Время движения (ч): 3
# Пройденное расстояние: 240 км
#
# Входные данные	Ожидаемый ответ
# speed	time	distance
# 80	3	240
# 110	5	550
# 30	1	30
# В заданиях по программированию обычно указывают примеры входных и выходных данных программы.
# Вы должны написать такую программу, чтобы для каждого примера входных данных она выдала ожидаемый ответ.
#
# Если хотя бы в одном случае ответ не совпадает с ожидаемым, то программа считается написанной неправильно.

speed = int(input())
time = int(input())
distance = speed * time

print(f"Скорость движения (км/ч): {speed}\n" +
      f"Время движения (ч): {time}\n" +
      f"Пройденное расстояние: {distance} км")






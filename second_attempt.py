# with open("weather2.csv", encoding="utf-8") as file:
#     file.readline().split(";")
#     file.readline().split(";")
#     file.readline().split(";")
#     file.readline().split(";")
#     file.readline().split(";")
#     file.readline().split(";")
#     title = file.readline().split(";")
#     print(title)
#
#     i_date = title.index('"Местное время в Шереметьево / им. А. С. Пушкина (аэропорт)"')
#     i_temp = title.index('"T"')
    # i_p_min = title.index('"P0"')
    # i_p = title.index('"P"')
    # i_u = title.index('"U"')
    # i_ff = title.index('"Ff"')

    # weather_day =dict()
    # weather_day_temp =dict()
    #
    # weather_day_average_temp = dict()

    # weather = dict()
    # count_day = dict()

    # Не знаю как перезаписать в словарь
    # for line in file:
    #     data = line.split(";")
    #
    #     date, time = data[i_date].strip("\"").split()
    #     day, month, year = date.split(".")
    #     temp = data[i_temp].strip("\"")
    #     if temp == "":
    #         continue
    #     temp = float(temp)

        # Может среднюю за день, а потом за месяц

        # weather_day_temp[day] = weather_day_temp.get(day, 0) + temp

        # if month not in weather:
        #     weather[month] = []
        # weather[month].append(temp)
    # print(weather)
    # for month in weather:
    #     weather[month] = sum(weather[month]) / len(weather[month])
    # for month in sorted(weather):
    #     print(round(weather[month], 1))
    # for key, values in count_day.items():
    #     count_day2[key] = len(values)
    #
    # print(count_day2)
    #
    # for key, value in weather.items():
    #     this_count_day = count_day2[key]
    #     average_temp = value / this_count_day
    #     print(average_temp)


# ZJ: Мужские имена - wat?!


# with open("man_name_2.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"Name"')
#
#     file.readline()
#
#     names = []
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#
#         if name.islower():
#             names.append(name)
#
#     for name in names:
#         print(name.capitalize())

# D: Средний балл по классам

# Иванов Сергей 9 90
# Сергеев Петр 10 91
# Петров Василий 11 92
# Васильев Иван 9 93



# with open("data.csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"name"')
#     i_class = title.index('"class"')
#     i_ball = title.index('"ball"')
#
#     ball_in_class = dict()
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name]
#         classs = data[i_class]
#         ball = int(data[i_ball].strip("\""))
#
#         # if name in students:
#         #     students[name][classs] = ball
#         #         # {'"Иванов Сергей"': {"9": 90, "10": 54}
#         # else:
#         #     students[name] = dict()
#
#         if classs not in ball_in_class:
#             ball_in_class[classs] = []
#         ball_in_class[classs].append(ball)
#         # Дольше
#         # if classs in ball_in_class:
#         #     ball_in_class[classs].append(ball)
#         # else:
#         #     ball_in_class[classs] = [ball]
#
#     for classs, ball in ball_in_class.items():
#         total = sum(ball)
#         count = len(ball)
#         print(total / count)


# E: Количество победителей по классам
# with open("data.csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"name"')
#     i_school = title.index('"class"')
#     i_ball = title.index('"ball"')
#
#     prize_ball = dict()
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name]
#         classs = data[i_school]
#         ball = int(data[i_ball].strip("\""))
#
#         if classs not in prize_ball:
#             prize_ball[classs] = []
#         prize_ball[classs].append(ball)
#
#     print(prize_ball)
#     max_ball = dict()
#     for key in prize_ball.keys():
#         max_ball[key] = max(prize_ball[key])
#     print(max_ball)
#
#     count_class = dict()
#     for key, value in prize_ball.items():
#         print(value, max_ball[key])
#         for ball in value:
#             if ball == max_ball[key]:
#                 count_class[key] = count_class.get(key, 0) + 1
#     print(count_class)
#
#     for value in count_class.values():
#         print(value, end=" ")

# F: Победитель олимпиады TODO
# with open("data2.csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"name"')
#     i_school = title.index('"class"')
#     i_ball = title.index('"ball"')
#
#     ball_in_name = dict()
#     name = []
#     max_ball = 0
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         classs = data[i_school]
#         ball = int(data[i_ball].strip("\""))
#
#         if ball not in ball_in_name:
#             ball_in_name[ball] = []
#         ball_in_name[ball].append(name)
#
#     ball_in_name_list = list(ball_in_name.items())
#     ball_in_name_list.sort(reverse=True)
#     if len(ball_in_name_list[0][1]) > 1:
#         print(len(ball_in_name_list[0][1]))
#     else:
#         print(*ball_in_name_list[0][1])

# 2  попытка TODO F: Победитель олимпиады
with open("data2.csv", encoding="utf-8") as file:
    title = file.readline().split(";")
    print(title)

    i_name = title.index('"name"')
    i_ball = title.index('"ball"')

    max_ball = 0
    winners = []

    for line in file:
        data = line.split(";")

        name = data[i_name].strip("\"")
        score = int(data[i_ball].strip("\""))

        if score > max_ball:
            max_ball = score
            winners.clear()
            winners.append(name)
        elif score == max_ball:
            winners.append(name)

    if len(winners) > 1:
        print(len(winners))
    else:
        print(*winners)


# G: Максимальный балл не-победителя
# with open("data3.csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"name"')
#     i_class = title.index('"class"')
#     i_ball = title.index('"ball"')
#
#     ball_in_class = dict()
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         classs = data[i_class]
#         ball = int(data[i_ball].strip("\""))
#
#         if classs not in ball_in_class:
#             ball_in_class[classs] = []
#         ball_in_class[classs].append(ball)
#
#     ball_in_class_list = list(ball_in_class.items())
#     print(ball_in_class_list)
#
#       # Отсортировать по убыванию
#     for key in ball_in_class.keys():
#         ball_in_class[key].sort(reverse=True)
#         max_value = ball_in_class[key][0]
#         for value in ball_in_class[key]:
#             if value != max_value:
#                 print(value, end=" ")
#                 break

    # Найти первое число не равное макс в каждом классе и break
    # вывести эти значения

    # print(ball_in_class_list)


# H: Максимальный балл призера и их количество TODO

# with open("data4.csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"name"')
#     i_school = title.index('"class"')
#     i_ball = title.index('"ball"')
#
#     all_ball = dict()
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         classs = data[i_school]
#         ball = int(data[i_ball].strip("\""))
#
#         if ball not in all_ball:
#             all_ball[ball] = []
#         # prize_ball[ball] = prize_ball.get(ball, 0) + 1 - почему-то не получилось так сделать
#         all_ball[ball].append(name)
#
#     max_ball = max(all_ball.keys())
#     all_balls = all_ball.keys()
#     all_balls_sort = sorted(all_balls, reverse=True)
#     prize_ball = 0
#         # Отсортировали
#         # Значит нам не страшны повторения, хотя их тут нет)
#         # И получается следующее значение это балл для призёров
#     for ball_i in all_balls_sort:
#         if ball_i != max_ball:
#             prize_ball = ball_i
#             break
#     count_participants = len(all_ball[prize_ball])
#     print(prize_ball, count_participants)

# max_1 = 0
# max_2 = 0
#
# max_1 = new_max
# max_2 = max_1

# Второй вариант TODO H: Максимальный балл призера и их количество
with open("data4.csv", encoding="utf-8") as file:
    title = file.readline().split(";")
    print(title)

    i_name = title.index('"name"')
    i_ball = title.index('"ball"')

    winners_score = 0
    prize_score = 0
    # Сделал с двумя массивами, можно по-другому
    people_prize = []
    people_winners = []
    for line in file:
        data = line.split(";")

        name = data[i_name].strip("\"")
        score = int(data[i_ball].strip("\""))

        if score > winners_score:
            prize_score = winners_score
            winners_score = score
            people_prize = people_winners
            people_winners = []

        if score == winners_score:
            people_winners.append(name)
    print(prize_score, len(people_prize))


# I: Имя наилучшего не-победителя #  TODO список
# with open("data5.csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"name"')
#     i_school = title.index('"class"')
#     i_ball = title.index('"ball"')
#
#     all_ball = dict()
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         classs = data[i_school]
#         ball = int(data[i_ball].strip("\""))
#
#         if ball not in all_ball:
#             all_ball[ball] = []
#         # prize_ball[ball] = prize_ball.get(ball, 0) + 1 - почему-то не получилось так сделать
#         all_ball[ball].append(name)
#
#     max_ball = max(all_ball.keys())
#     all_balls = all_ball.keys()
#     all_balls_sort = sorted(all_balls, reverse=True)
#     prize_ball = 0
#         # Отсортировали
#         # Значит нам не страшны повторения, хотя их тут нет)
#         # И получается следующее значение это балл для призёров
#     for ball_i in all_balls_sort:
#         if ball_i != max_ball:
#             prize_ball = ball_i
#             break
#     count_participants = len(all_ball[prize_ball])
#     if count_participants > 1:
#         print(count_participants)
#     else:
#         print(*all_ball[prize_ball])

# Второй вариант TODO I: Имя наилучшего не-победителя
with open("data5.csv", encoding="utf-8") as file:
    title = file.readline().split(";")
    print(title)

    i_name = title.index('"name"')
    i_ball = title.index('"ball"')

    winners_score = 0
    prize_score = 0
    # Сделал с двумя массивами, можно по-другому
    people_prize = []
    people_winners = []

    for line in file:
        data = line.split(";")

        name = data[i_name].strip("\"")
        score = int(data[i_ball].strip("\""))

        if score > winners_score:
            prize_score = winners_score
            winners_score = score
            people_prize = people_winners
            people_winners = [name]
        elif score == winners_score:
            people_winners.append(name)
        elif score > prize_score:
            prize_score = score
            people_prize = [name]
        elif score == prize_score:
            people_prize.append(name)

    if len(people_prize) > 1:
        print(len(people_prize))
    else:
        print(*people_prize)
# Не работает с такими данными
# "ID";"name";"class";"ball";
# "1";"Иванов Сергей";"9";"92";
# "2";"Сергеев Петр";"10";"91";
# "3";"Петров Василий";"11";"92";
# "4";"Васильев Иван";"9";"93";

# J: Школы с наибольшим числом участников олимпиады

# with open("data6.csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"name"')
#     i_school = title.index('"school"')
#     i_ball = title.index('"ball"')
#
#     all_school = dict()
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         school = data[i_school].strip("\"")
#         ball = int(data[i_ball].strip("\""))
#
#         if school not in all_school:
#             all_school[school] = 0
#         all_school[school] += 1
#     print(all_school)
#
#     max_student = max(all_school.values())
#     # Не смог решить через лямбдо-сортировку, поэтому создал массив и отсортировал его
#     best_school = []
#     for key in all_school.keys():
#         if all_school[key] == max_student:
#             best_school.append(int(key))
#     best_school.sort(reverse=True)
#     print(*best_school)

# max_1 = 0
# max_2 = 0
#
# max_1 = new_max
# max_2 = max_1


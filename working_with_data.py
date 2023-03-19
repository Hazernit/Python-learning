# with open("ejudge1 (1).csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#     # print(title)
#     # title[21] - User_Id, title[22] - User_Login
#
#     User_Id = title.index("User_Id")
#     User_Login = title.index("User_Login")
#     User_Inv = title.index("User_Inv")
#     Lang = title.index("Lang")
#     Score = title.index("Score")
#
#     entity_dict = dict()
#     for line in file:
#         # print(line)
#         date = line.split(";")
#         print(date)
#         a_user_login = date[User_Login]
#         a_user_inv = date[User_Inv]
#         a_score = date[Score]
#         a_lang = date[Lang]
#
#         if date[User_Inv] == "I":
#             continue
#         if int(a_score) <= 0:
#             continue
#         if a_lang in entity_dict:
#             entity_dict[a_lang].add(a_user_login)
#         else:
#             entity_dict[a_lang] = {a_user_login}
#
#     # print(entity_dict)
#     all_users = set.union(*entity_dict.values())  # Объеденение всего
#     total_participants = len(all_users)
#     print(f"Total: {total_participants}")
#     print(entity_dict)
#     for key in entity_dict:
#         entity_dict[key] = len(entity_dict[key])
#
#     items = list(entity_dict.items())
#     print(items)
#     print()
#
#     items.sort()
#     # {"car": "Mercedes",
#     # "car2":"BMW",
#     # "car3":"Audi" }
#
#     items.sort(key=lambda x: -x[1])
#     for key, values in items:
#         print(f"{key}: {values}")


# Альтернатива (очень долгий метод)
# print("total_participants")
#
# data_array = []
# for key, values in entity_dict.items():
#     data_array.append(list(values))
# print("data_array")
# print(data_array)
# print(len(data_array))
# new_data_array = []
# for i in range(len(data_array)):
#     for j in range(len(data_array[i])):
#         new_data_array.append(data_array[i][j])
# print(new_data_array)
# print(len(new_data_array))
# set_data_array = set(new_data_array)
# print(set_data_array)
# print(len(set_data_array))
# total_participants = entity_dict.values()
# print(total_participants)
# print(len(total_participants))

# B: Ejudge: результаты личной олимпиады
# with open("ejudge1 (1).csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#
#     i_login = title.index("User_Login")
#     i_user_name = title.index("User_Name")
#     i_score = title.index("Score")
#     i_prob = title.index("Prob")
#     i_inv = title.index("User_Inv")
#
#     tasks_marks = dict()
#     login_to_name = dict()
#     for line in file:
#         date = line.split(";")
#
#         login = date[i_login]
#         user_name = date[i_user_name]
#         score = int(date[i_score])
#         prob = date[i_prob]
#
#         if score == -1:
#             continue
#
#         if date[i_inv] == "I":
#             continue
#
#         login_to_name[login] = user_name
#         if login in tasks_marks:
#             if prob in tasks_marks[login]:
#                 tasks_marks[login][prob] = max(tasks_marks[login][prob], score)
#             else:
#                 tasks_marks[login][prob] = score
#         else:
#             tasks_marks[login] = {prob: score}


# for login in tasks_marks:
#     print(login)
#     tasks_marks[login] = sum(tasks_marks[login].values())
#     print(tasks_marks)

# print(tasks_marks.items())

# for key, value in login_to_name.items():
#     for key2 in tasks_marks.keys():
#         if key == key2:
#             print(key2)
#             print(value)
#             print(tasks_marks[key])
#             print(tasks_marks[key].values())
#             print(sum(tasks_marks[key].values()))
#             print()
#
# names_points = dict()
# for key, value in login_to_name.items():
#     for key2 in tasks_marks.keys():
#         if key == key2:
#             names_points[value] = sum(tasks_marks[key].values())
# tasks_marks[key]["name"] = value
# print(value, sum(tasks_marks[key].values()))
# print(names_points.items())

# sorted_names_points = dict(sorted(names_points.items(), key=lambda item: -item[1]))
#
# print(sorted_names_points)

# for key, value in sorted_names_points.items():
#     print(f"{key}: {value}")


# C: Ejudge: результаты командной олимпиады

# with open("ejudge2 (1).csv", encoding="utf-8") as file:
#     title = file.readline().split(";")
#
#     i_short = title.index("Stat_Short")
#     i_dour = title.index("Dur")
#     i_dour_min = title.index("Dur_Min")
#     i_dour_hour = title.index("Dur_Hour")
#     i_user_name = title.index("User_Name")
#     i_prob = title.index("Prob")
#     i_start_short = title.index("Stat_Short")
#     i_user_inv = title.index("User_Inv")
#
#     decisions = dict()
#     for line in file:
#         date = line.split(";")
#
#         user_name = date[i_user_name]
#         start_short = date[i_short] == "OK"
#         if date[i_start_short] == "CE":
#             continue
#         if date[i_user_inv] == "I":
#             continue
#         minute = int(date[i_dour_hour]) * 60 + int(date[i_dour_min])
#         prob = date[i_prob]
#
#         if user_name in decisions:
#             if prob in decisions[user_name]:
#                 decisions[user_name][prob].append((minute, start_short))
#             else:
#                 decisions[user_name][prob] = [(minute, start_short)]
#         else:
#             decisions[user_name] = {prob: [(minute, start_short)]}
#
#     users_mistakes = dict()
#
#     for user_name in decisions.keys():
#         # print(user_name)
#
#         count_solved_problems = 0
#         # print(decisions[user_name])
#
#         for array_task in decisions[user_name]:
#             # print("item")
#             time = -1
#             penalty_minutes = 0
#             count_mistakes = 0
#             for item in decisions[user_name][array_task]:
#                 is_it_decided = item
#                 if not is_it_decided[1]:
#                     count_mistakes += 1
#                 if is_it_decided[1]:
#                     count_solved_problems += 1
#                     time = is_it_decided[0]
#                 # print(is_it_decided[1], time)
#
#             if time > -1:
#                 penalty_minutes += time + count_mistakes * 20
#
#         users_mistakes[user_name] = (count_solved_problems, penalty_minutes)
#     #     print(count_mistakes)
#     # print(users_mistakes)
#     # print(decisions[user_name].values())
#
#     list_users = list(users_mistakes.items())
#     print(list_users)
#     print()
#     list_users.sort()
#     list_users.sort(key=lambda x: x[1][1])
#     list_users.sort(key=lambda x: -x[1][0])
#     print(list_users)
#
#     for line in list_users:
#         print(*line)
    # for key in sorted(users_mistakes.keys()):
        # print(key, users_mistakes[key])
        # print(users_mistakes[key][0])

# D: Городской Wi-Fi

# with open("data-9776-2021-12-08.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     # print(title)
#
#     i_district = title.index('"District"')
#     i_Latitude_WGS84 = title.index('"Latitude_WGS84"')
#     i_NumberOfAccessPoints = title.index('"NumberOfAccessPoints"')
#
#     number_of_access_points = dict()
#
#     for line in file:
#         date = line.split(";")
#
#         district = date[i_district]
#         NumberOfAccessPoints = int(date[i_NumberOfAccessPoints].strip("\""))
#
#         number_of_access_points[district] = number_of_access_points.get(district, 0) + NumberOfAccessPoints
#
#     list_number_of_access_points = list(number_of_access_points.items())
#     #     print(list_users)
#     #     print()
#     list_number_of_access_points.sort()
#     list_number_of_access_points.sort(key=lambda x: -x[1])
#     for line in list_number_of_access_points:
#         print(*line)

            # if user_name in decisions:
        #             if prob in decisions[user_name]:
        #                 decisions[user_name][prob].append((minute, start_short))
        #             else:
        #                 decisions[user_name][prob] = [(minute, start_short)]
        #         else:
        #             decisions[user_name] = {prob: [(minute, start_short)]}

# E: Призёры регионального этапа всероссийской олимпиады в 2020/2021 году
# with open("data-27257-2022-02-02.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_short_name = title.index('"ShortName"')
#     i_status = title.index('"Status"')
#     i_stage = title.index('"Stage"')
#     i_year = title.index('"Year"')
#     count_winner = 0
#     prize_winner = 0
#
#     winners = dict()
#     file.readline()
#
#     for line in file:
#
#         data = line.split(";")
#
#         short_name = data[i_short_name]
#         status = data[i_status]
#         stage = data[i_stage]
#         year = data[i_year]
#
#         if stage != '"3"':
#             continue
#
#         if year != '"2020/2021"':
#             continue
#
#         if short_name not in winners:
#             winners[short_name] = [0, 0]
#         if status == '"призёр"':
#             winners[short_name][1] += 1
#         else:
#             winners[short_name][0] += 1
#
# items = list(winners.items())
# items.sort(key=lambda x: (-x[1][0] - x[1][1], -x[1][0], x[0]))
#
# for name, (w, pr) in items:
#     print(name + ":", w, pr)

# F: Предметы московской олимпиады

# with open("new2.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     # print(title)
#
#     i_subject = title.index('"Subject"')
#     i_year = title.index('"Year"')
#
#     count_year = dict()
#     file.readline()
#
#     for line in file:
#
#         data = line.split(";")
#
#         subject = data[i_subject]
#         year = data[i_year].strip("\"")
#
#         check_year = year[:4]
#
#         if int(check_year) < int(2012):
#             continue
#
#         if subject not in count_year:
#             count_year[subject] = {year}
#         count_year[subject].add(year)
#
# for key in count_year.keys():
#     count_year[key] = len(count_year[key])
#
# items = list(count_year.items())
# items.sort()
# # print(items)
# for subject, count in items:
#     subject = str(subject).strip("\"")
#     print(f"{subject}: {count}")
# print(items)
# print()
# print(items[1][2])
# items.sort(key=lambda x: x[0][0])


# print(count_year)

# G: «Качество» призёров регионального этапа
# max_year = 0
# with open("new2.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     # print(title)
#
#     i_short_name = title.index('"ShortName"')  # Название школы
#     i_year = title.index('"Year"')
#     i_status = title.index('"Status"')
#     i_stage = title.index('"Stage"')
#
#     free_stage = dict()
#     four_stage = dict()
#     file.readline()
#
#     for line in file:
#
#         data = line.split(";")
#
#         year = data[i_year]
#
#         check_year = year.strip("\"")
#         year = int(check_year[:4])
#
#         if year > max_year:
#             max_year = year
#
# with open("new2.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     # print(title)
#
#     i_short_name = title.index('"ShortName"')  # Название школы
#     i_year = title.index('"Year"')
#     i_status = title.index('"Status"')
#     i_stage = title.index('"Stage"')
#
#     free_stage = dict()
#     four_stage = dict()
#     file.readline()
#
#     for line in file:
#         data = line.split(";")
#
#         year = data[i_year]
#         year = year.strip("\"")
#         year = int(year[:4])
#
#         short_name = data[i_short_name]
#         stage = data[i_stage].strip("\"")
#         status = data[i_status].strip("\"")
#
#         if year < max_year:
#             continue
#
#         if stage == "":
#             continue
#         stage = int(stage)
#
#         if stage == 3 and (status == "призёр" or status == "победитель"):
#             free_stage[short_name] = free_stage.get(short_name, 0) + 1
#
#         if stage == 4 and (status == "призёр" or status == "победитель"):
#             four_stage[short_name] = four_stage.get(short_name, 0) + 1
#
#     answer = dict()
#     for key in free_stage.keys():
#         if key in four_stage:
#             free_stage_local = free_stage[key]
#             four_stage_local = four_stage[key]
#             attitude = four_stage_local/free_stage_local
#             if key not in answer:
#                 answer[key] = (free_stage_local, four_stage_local, attitude)
#
#     answer_items = list(answer.items())
#     answer_items.sort(key=lambda x: (-x[1][2], x[0]))
#
#     for i in range(len(answer_items)):
#         name = answer_items[i][0].strip("\"")
#         first_meaning = answer_items[i][1][0]
#         second_meaning = answer_items[i][1][1]
#         attitude = answer_items[i][1][2]
#
#         print(f"{name}: {first_meaning} {second_meaning} {attitude}")

    # for key, value in answer.items():
    #     name = key.strip("\"")
    #     print(f"{name}:", *value)

# H: Мужские имена

# with open("man_name.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_id = title.index('"ID"')  # Название школы
#     i_name = title.index('"Name"')  # Название школы
#     i_month = title.index('"Month"')  # Название школы
#     i_number_of_persons = title.index('"NumberOfPersons"')  # Название школы
#
#     total_newborns = dict()
#
#     for line in file:
#         data = line.split(";")
#
#         id_people = data[i_id]
#         name = data[i_name]
#         month = data[i_month]
#         number_of_persons = data[i_number_of_persons]
#         number_of_persons = number_of_persons.strip("\"")
#
#         if number_of_persons == "NumberOfPersons":
#             continue
#
#         number_of_persons = int(number_of_persons)
#
#         total_newborns[name] = total_newborns.get(name, 0) + number_of_persons
#
#     answer = list(total_newborns.items())
#     answer.sort(key=lambda x: (-x[1], x[0]))
#
#     for name, count in answer:
#         name = name.strip("\"")
#         print(f"{name}: {count}")

    # for i in range(len(answer)):
    #     name = answer[i][0]
    #     count =
    #     print()


# I: Мужские имена — убрать дубликаты

# with open("man_name.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_id = title.index('"ID"')  # Название школы
#     i_name = title.index('"Name"')  # Название школы
#     i_month = title.index('"Month"')  # Название школы
#     i_number_of_persons = title.index('"NumberOfPersons"')  # Название школы
#
#     total_newborns = dict()
#     new_names = dict()
#
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         # print(name)
#         if name == "Name":
#             continue
#         if "," in name:
#             name, *another_names = name.split(", ")
#             for n in another_names:
#                 new_names[n] = name
#
#         number_of_persons = data[i_number_of_persons]
#         number_of_persons = number_of_persons.strip("\"")
#         number_of_persons = int(number_of_persons)
#
#         total_newborns[name] = total_newborns.get(name, 0) + number_of_persons
#
#     for name in new_names.keys():
#         if name in total_newborns:
#             right_name = new_names[name]
#             total_newborns[right_name] = total_newborns.get(right_name, 0) + total_newborns[name]
#             del total_newborns[name]
#
#     # print(new_names)
#
#     answer = list(total_newborns.items())
#     answer.sort(key=lambda x: (-x[1], x[0]))
#
#     for name, count in answer:
#         print(f"{name}: {count}")



# test = "dsfs,sd,f"
# first, *tests = test.split(",")
#
# print(first)
#
# test = "dsfs,sd,f"
# start = test.find(",")
# test = test[:start]
# print(test)

# K: Мужские имена — среднее значение
# total_artem = 0
# with open("man_name.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"Name"')
#     i_month = title.index('"Month"')
#     i_year = title.index('"Year"')
#     i_number_of_persons = title.index('"NumberOfPersons"')
#
#
#     total_newborns = dict()
#     new_names = dict()
#     count_month = dict()
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         if name == "Name":
#             continue
#         # if "," in name:
#         #     name, *another_name = name.split(", ")
#
#             # for n in another_name:
#             #     new_names[n] = name
#
#         number_of_persons = int(data[i_number_of_persons].strip("\""))
#
#         if name == "Артём":
#             total_artem += number_of_persons
#         month = data[i_month]
#
#         total_newborns[name] = total_newborns.get(name, 0) + number_of_persons
#
#         for name in new_names.keys():
#             if name in total_newborns:
#                 right_name = new_names[name]
#                 total_newborns[right_name] = total_newborns.get(right_name, 0) + total_newborns[name]
#                 del total_newborns[name]
#     print("Artem total = ", total_artem)
#     answer = list(total_newborns.items())
#
#     answer.sort(key=lambda x: (-x[1], x[0].lower()))
#     for name, total in answer:
#         print(name + ": " + str(total))

    # for name, total in total_newborns.items():
    #     print(f"{name}: {total}")

# K: Мужские имена — среднее значение
# with open("man_name.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"Name"')
#     i_month = title.index('"Month"')
#     i_year = title.index('"Year"')
#     i_number_of_persons = title.index('"NumberOfPersons"')
#
#     another_names = dict()
#     total_newborns = dict()
#     average_newborns = dict()
#
#     borns = dict()
#
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         if name == "Name":
#             continue
#
#         month = data[i_month].strip("\"")
#         year = data[i_year].strip("\"")
#         number_of_persons = int(data[i_number_of_persons].split("\"")[1])
#
#         count_month = "количество месяцев"
#
#         if "," in name:
#             name, *another_name = name.split(", ")
#
#             for n in another_name:
#                 another_names[n] = name
#
#         # for name in another_names.keys():
#         #     if name in total_newborns:
#         #         right_name = another_names[name]
#         #         total_newborns[right_name] = total_newborns.get(right_name, 0) + total_newborns[name]
#         #         del total_newborns[name]
#
#         if name not in borns:
#             borns[name] = {}
#             # "Александр" : {}
#         if (year, month) not in borns[name]:
#             borns[name][(year, month)] = 0
#             # "Александр" : {(year, month)}
#
#         borns[name][(year, month)] += number_of_persons
#         # "Александр" : {(year, month): x + number_of_persons}
#
#
#     for name in another_names:
#         if name not in borns:
#             borns[name] = dict()
#         for (year, month) in borns[name]:
#             borns[another_names[name]][(year, month)] += borns[name][(year, month)]
#         del borns[name]
#
#     for name in borns:
#         for (year, month) in borns[name]:
#             print(name, year, month, borns[name][(year, month)])
#
#     print(borns)
#
#     for name in borns:
#         borns[name] = sum(borns[name].values()) // len(borns[name])
#         # borns[name].values() - 275, 301
#         # sum(borns[name].values()) - 275 + 301
#         # borns[name] - 2015 сентябрь 275, 2015 октябрь 301, 2015 ноябрь 267
#         # len(borns[name]) = 3 (т.к. длина всех значений по ключу)
#
#     items = list(borns.items())
#     items.sort(key=lambda x: (-x[1], x[0]))
#
#     for name, count in items:
#         print(name, count)



                                #  количество детей,          количество месяцев
        # total_newborns[name] = [total_newborns.get(name, 0)[0] + number_of_persons, 0]
        # total_newborns[name].append(total_newborns.get(name, 0) + number_of_persons)

        # Почему вот это сработало, а нижнее нет
        # if short_name not in winners:
        #             winners[short_name] = [0, 0]
        #         if status == '"призёр"':
        #             winners[short_name][1] += 1
        #         else:
        #             winners[short_name][0] += 1

        # if number_of_persons > 0:
        #     total_newborns[name][1] += 1
        #
        # for name in total_newborns.keys():
        #     average_newborns[name] = math.floor(total_newborns[name][0] / total_newborns[name][1])

    # print(total_newborns)


# TODO L: Мужские имена — динамика по времени

# first_year = 200002
# last_year = 0
# with open("man_name.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"Name"')
#     i_month = title.index('"Month"')
#     i_year = title.index('"Year"')
#     i_number_of_persons = title.index('"NumberOfPersons"')
#
#     another_names = dict()
#     total_newborns = dict()
#     average_newborns = dict()
#
#     borns = dict() # burns
#
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         if name == "Name":
#             continue
#
#         month = data[i_month].strip("\"")
#         year = data[i_year].strip("\"")
#         number_of_persons = int(data[i_number_of_persons].split("\"")[1])
#
#         if "," in name:
#             name, *another_name = name.split(", ")
#
#             for n in another_name:
#                 another_names[n] = name
#
#         if name not in borns:
#             borns[name] = {}
#
#         if (year, month) not in borns[name]:
#             borns[name][(year, month)] = 0
#
#         borns[name][(year, month)] += number_of_persons
#
#         for name in another_names:
#             if name not in borns:
#                 borns[name] = dict()
#             for (year, month) in borns[name]:
#                 borns[another_names[name]][(year, month)] += borns[name][(year, month)]
#             del borns[name]
#
#     for name, values in borns.items():
#         first_year = float("inf")
#         last_year = float("-inf")
#         first_n_months = 0
#         last_n_months = 0
#         first_n_people = 0
#         last_n_people = 0
#         for (year, month), count_borns in borns[name].items():
#             # print(name, borns[name][(year, month)])
#             year = int(year)
#             if first_year > year:
#                 first_year = year
#                 first_n_months = 1
#                 first_n_people = count_borns
#             elif first_year == year:
#                 first_n_months += 1
#                 first_n_people += count_borns
#             if last_year < year:
#                 last_year = year
#                 last_n_months = 1
#                 last_n_people = count_borns
#             elif last_year == year:
#                 last_n_months += 1
#                 last_n_people += count_borns
#         average_first = first_n_people // first_n_months
#         average_last = last_n_people // last_n_months
#         borns[name] = (average_first, average_last, average_last-average_first)
#
#     answer = list(borns.items())
#     answer.sort(key=lambda x: (-x[1][2]))
#
#
#     for name, values in answer:
#         print(name + ":", *values)


# M: Призёры регионального этапа всероссийской олимпиады за пять лет

# with open("new2.csv", encoding="cp1251") as file:
#     title = file.readline().split(";")
#     print(title)
#
#     i_name = title.index('"ShortName"')
#     i_year = title.index('"Year"')
#     i_status = title.index('"Status"')
#     i_global_id = title.index('"global_id"')
#
#     file.readline()
#
#     winners = dict()
#     prize_winners = dict()
#
#     for line in file:
#         data = line.split(";")
#
#         name = data[i_name].strip("\"")
#         year = int(data[i_year].strip("\"")[:4])
#         status = data[i_status].strip("\"")
#         print(status)
#
#
#         if year < 2015 or year > 2019:
#             continue
#
#         if status == "победитель":
#             winners[name] = winners.get(name, 0) + 1
#         if status == "призёр":
#             prize_winners[name] = prize_winners.get(prize_winners, 0) + 1



        # if name in winners:
        #     if year in winners[name]:
        #         winners[name][year] += 1
        #         print(winners)
        # else:
        #     prize_winners_and_winners[name][year] = 0

    # print(winners)

# N: Ближайшая точка доступа к школе
#
# import json
#
# f = open('school2.json')
#
# data = json.load(f)
# LegalAddress
# ShortName

# for line in data:
#     legal_address = line["LegalAddress"]
#     short_name = line["ShortName"]
#     if "№ 179" in short_name:
#         print(legal_address, short_name)
#         our_address = legal_address
#
#
# f.close()

# with open("new2.csv", encoding="cp1251") as file:
#     title = file.readline().replace("\"", "")
#     title = title.split(";")
#
#     i_short_name = title.index("ShortName")
#
#
#
# with open("wi-fi.csv", encoding="cp1251") as file:
#     title = file.readline().replace("\"", "")
#     title = title.split(";")
#     print(title)
#
#     i_location = title.index("Location")
#     print(i_location)
#
#     file.readline()
#
#     for line in file:
#
#         data = line.split(";")
#         location = data[i_location]
#         print(location)

# O: Архив погодных данных

with open("weather2.csv", encoding="utf-8") as file:
    file.readline().split(";")
    file.readline().split(";")
    file.readline().split(";")
    file.readline().split(";")
    file.readline().split(";")
    file.readline().split(";")
    title = file.readline().split(";")
    print(title)

    i_date = title.index('"Местное время в Шереметьево / им. А. С. Пушкина (аэропорт)"')
    i_temp = title.index('"T"')
    # i_p_min = title.index('"P0"')
    # i_p = title.index('"P"')
    # i_u = title.index('"U"')
    # i_ff = title.index('"Ff"')

    weather = dict()
    count_day = dict()

    # Не знаю как перезаписать в словарь
    count_day2 = dict()

    for line in file:

        data = line.split(";")

        full_date = data[i_date].strip("\"").split()
        time = full_date[1]
        date = full_date[0].split(".")
        day = date[0]
        month = date[1]
        temp = data[i_temp].strip("\"")
        if temp == "":
            continue
        temp = float(temp)

        weather[month] = weather.get(month, 0) + temp
        if month in count_day:
            count_day[month].append(day)
        else:
            count_day[month] = []

        # Может среднюю за день, а потом за месяц
        # Было
        # if month in count_day:
        #     count_day[month].add(day)
        # else:
        #     count_day[month] = set()

    print(weather)

    for key, values in count_day.items():
        count_day2[key] = len(values)

    print(count_day2)

    for key, value in weather.items():
        this_count_day = count_day2[key]
        average_temp = value / this_count_day
        print(average_temp)
# Я не понимаю как создавать словарь в словаре
# Например
# december: {temp: 8, count_day: 11, descr: { other: "sdfsdf", inyeresting_fact: "dafsdf"}}

december = dict()

december["temp"] = 0
december["count_day"] = 11

december["descr"] = dict()

december["descr"]["other"] = "sdfsdf"
december["descr"]["inyeresting_fact"] = "dafsdf"
# Пытался так, но безуспешно (
# if month in weather:
#     if "count" in weather[month]:
#         weather[month]["sum"] += temp
#         weather[month]["count"] += 1
#     else:
#         weather[month]["count"] = 0
#         weather[month]["count"] = "sum"
# else:
#     weather[month] = dict()
#     weather[month]["count"] = 0


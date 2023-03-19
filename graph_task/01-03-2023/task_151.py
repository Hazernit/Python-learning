from collections import deque


# from time import sleep

def can_seat(person, table):
    for i in range(len(persons)):
        if persons[i] == table and matrix[person][i] == 0:
            return False
    return True


n, m = map(int, input().split())

matrix = [[1] * n for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    matrix[i - 1][j - 1] = 0
    matrix[j - 1][i - 1] = 0

persons = [0] * n
want_to_plant = deque()

is_seat = True
for num_person in range(n):

    if persons[num_person] != 0:
        continue

    if can_seat(num_person, -1):
        want_to_plant.append((num_person, -1))
        persons[num_person] = -1
    elif can_seat(num_person, 1):
        want_to_plant.append((num_person, 1))
        persons[num_person] = 1
    else:
        is_seat = False
        break

    while want_to_plant:
        # print(want_to_plant)
        # sleep(0.3)
        i, table = want_to_plant.popleft()

        for j in range(n):
            if matrix[i][j] == 0 and persons[j] == 0:
                if not can_seat(j, -table):
                    is_seat = False
                    break
                want_to_plant.append((j, -table))
                persons[j] = -table
        if not is_seat:
            break
    if not is_seat:
        break

if is_seat:
    print("YES")
else:
    print("NO")



















# from collections import deque
#
# n, m = map(int, input().split())
#
# matrix = [[1] * n for _ in range(n)]
# # print(matrix)
#
# for _ in range(m):
#     i, j = map(int, input().split())
#     matrix[i-1][j-1] = 0
#     matrix[j-1][i-1] = 0
#
# want_to_plant1 = matrix
# want_to_plant2 = matrix
# planted1 = set()
# planted2 = set()
#
# is_seat = True
# for i in range(len(want_to_plant1)):
#     for j in range(len(want_to_plant1)):
#         if want_to_plant1[i][j] == 1:
#             planted1.add(i)
#             planted1.add(j)
#         else:
#             is_table_one = True
#             is_table_two = True
#             for t in planted1:
#                 if want_to_plant1[i][t] != 1:
#                     is_table_one = False
#             if is_table_one:
#                 planted1.add(i)
#             else:
#                 for t in planted2:
#                     if want_to_plant2[i][t] != 1:
#                         is_table_two = False
#                 if is_table_two:
#                     planted2.add(i)
#                 elif not is_table_one and not is_table_two:
#                     is_seat = False
#                     break
#             is_table_one = True
#             is_table_two = True
#             for t in planted1:
#                 if want_to_plant1[j][t] != 0:
#                     is_table_one = False
#             if is_table_one:
#                 planted1.add(j)
#             else:
#                 for t in planted2:
#                     if want_to_plant2[j][t] != 0:
#                         is_table_two = False
#                 if is_table_two:
#                     planted2.add(j)
#                 else:
#                     is_seat = False
#                     break
#
# if not is_seat:
#     print("YES")
# else:
#     print("NO")




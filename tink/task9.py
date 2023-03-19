# n = int(input())
#
# spending = []
# for _ in range(n):
#     money = int(input())
#     spending.append(money)
#
# coupon = []
# total = 0
# for i in range(len(spending)):
#     if spending[i] not in coupon:
#         total = spending[i]
#
#     while total >= 100:
#         index = 0
#         max_spend = 0
#         for j in range(i+1, len(spending)):
#             spend = spending[j]
#             if spend not in coupon and max_spend < spend:
#                 index = j
#                 max_spend = spend
#         coupon.append(max_spend)
#         total = 0
#
# total_money = sum(spending) - sum(coupon)
# print(total_money)

n = int(input())
# Создание таблички
matrix = [[0] * n for i in range(n)]

# индекс строки - номер обеда
# номер столбца - количество свободных купонов

# matrix = []
#
# for i in range():
#     row = []
#     for j in range():
#         row.append(j)
#     matrix.append(row)








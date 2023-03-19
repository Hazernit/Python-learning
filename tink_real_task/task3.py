#
# m = int(input())
#
# a, b = map(int, input().split())
# print(a)
# print(b)
#
# if a > b:
#     a %= b
#     print(a)
# else:
#     b %= a
#     print(b)
# print(m//(a+b))


number = int(input())

first_number = 0
for i in range(1, number//2+1):
    # print(i)
    if number % i == 0:
        first_number = i
second_number = number - first_number
print(first_number, second_number)



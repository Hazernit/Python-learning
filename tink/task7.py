
n_people = int(input())
peoples = list(map(int, input().split()))

number_set = set()
index1 = -1
index2 = -1
index = 1
for i in range(len(peoples)):
    index += i
    number = peoples[i]
    if number not in number_set:
        number_set.add(number)
    else:
        numbers_array = list(number_set)
        index1 = numbers_array.index(number) + 1
        index2 = number + 1
        break
    index = 1
print(index1, index2)


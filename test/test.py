from random import randint

# numbers = [randint(1, 10**18) for _ in range(2)]
# print(numbers)
# numbers.extend(randint(10, 99) for _ in range(10))
# print(numbers)
# numbers.extend(randint(100, 999) for _ in range(10))
# print(numbers)

numbers = [randint(1, 10 ** 18) for _ in range(2)]
numbers.sort()
l, r = numbers

print(l, r)















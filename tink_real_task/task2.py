a, b, c = map(int, input())

count_a, count_b, count_c = map(int, input())

count_a1, count_b1, count_c1 = a, b, c

count = 0

while count_a1 > 0:
    if count_a1 >= b:
        count_a1 -= b
        count_b1 += 1
        count += 1
    else:
        break

count_a1_1, count_b1_1, count_c1_1 = count_a1, count_b1, count_c1

while count_b1 > 0:
    if b >= c:
        b -= c
        c += 1
        count += 1






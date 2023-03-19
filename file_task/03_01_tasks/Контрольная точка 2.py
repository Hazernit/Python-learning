mark_1,	mark_2,	mark_3,	mark_4,	mark_5,	= map(int, input().split())

max_value = max(mark_1, mark_2, mark_3, mark_4, mark_5)
minimum_value = min(mark_1, mark_2, mark_3, mark_4, mark_5)
total = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5)

average_5 = total / 5
average_3 = (total - minimum_value - max_value) / 3
difference = abs(average_5 - average_3)

print("average_5:", average_5)
print("average_3:", average_3)
print("difference:", difference)




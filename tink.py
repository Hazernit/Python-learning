words = set(list(input()))
sort_words = sorted(words)
print(sort_words)

a = set(list(input()))

while a != "":
    words.difference_update(a)
    sort_words = sorted(words)
    print(sort_words)

    a = set(list(input()))

# test = ['a', 'б', 'в', 'г', 'д', 'е']
#
# for i in range(len(test)):
#     line = test[i]
#     for j in range(len(test)):
#         line += test[j]
#         for l in range(len(test)):
#             line += test[l]
#             # for m in range(len(test)):
#             #     line += test[m]
#             #     for k in range(len(test)):
#             #         line += test[k]
#             print(line)
#
#     print()

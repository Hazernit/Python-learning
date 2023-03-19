array = ["a", "b", "c", "d", "e", "f", "b", "a", "c", "a", "b", "c"]

count = 0
# word = 0
count_max = 0
word_max = 0
for i in range(len(array)):
    for j in range(i, len(array)):
        if array[i] == array[j]:
            # word = array[i]
            count += 1
            print(f"i = {i}, j = {j}, буква: {array[i]}")
    if count_max < count:
        word_max = array[i]  # word
        count_max = count
    count = 0

print(word_max, count_max)





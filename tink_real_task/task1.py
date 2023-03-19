count_word = int(input())

# words = list(map(str, input().split()))
words = input().split()

colour = input()
# print(colour)
# print()

words_colour_split = []

for word in words:
    word_split = colour[:len(word)]
    words_colour_split.append(word_split)
    colour = colour[len(word):]
    # print(colour)

# print(words_colour_split)

answer = 0
for colour in words_colour_split:
    for i in range(1, len(colour)):
        if colour[i] == colour[i-1]:
            answer += 1
            # print(colour)
            break
print(answer)

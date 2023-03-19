# for _ in range(3):
#     print("#", end="\n")

# inp = input()
# line = ""
# while inp != "":
#     line += inp
#     inp = input()

with open("input.txt") as f:

    result = ""
    for line in f:

        line = line.replace(" ", "")
        result += line
# print(line)
line = list(sorted(result))
# print(line)

words = {}
# print(type(words))
for i in line:
    words[i] = words.get(i, 0) + 1

# print(words)

max_value = 0
symbols = ""
for key, value in words.items():
    symbols += key
    if max_value < value:
        max_value = value

# print(max_value)

drawing = []
for _ in range(max_value):
    ans = ""
    for key in words.keys():
        if words[key] > 0:
            ans += "#"
            words[key] = words.get(key, 0) - 1
        else:
            ans += " "
    drawing.append(ans)

drawing.reverse()
for line_ans in drawing:
    print(line_ans)
print(symbols)



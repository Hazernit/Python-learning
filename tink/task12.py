
total = int(input())

denomination = list(map(int, input().split()))

our_total = 1

count = 0
for i in range(len(denomination)):
    while our_total <= total:
        our_total += denomination[i]
        if our_total <= total:
            count += 1
            print(denomination[i])
    print()
    if our_total > total:
        our_total = 1

for i in range(len(denomination)):
    this_total = 1
    for j in range(i+1, len(denomination)):
        this_total += denomination[i] + denomination[j]
        while total >= this_total:
            print(f"1 + {denomination[i]} + {denomination[j]} = {this_total}")
            count += 1

            j += 1
            if j >= len(denomination):
                break
            this_total += denomination[j]
            if this_total > total:
                # j -= 1
                this_total = 1 + denomination[i] + denomination[j]

print()
print(count)





















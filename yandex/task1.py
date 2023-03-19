a = int(input())

line = list(map(int, input().split()))
flag = True

for i in range(len(line)-1):
    if a[i] > a[i+1]:
        flag = False
        break

if flag:
    print(line[a-1] - a[0])
else:
    print(-1)





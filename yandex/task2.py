n = int(input())
eventsById = {}
for i in range(n):
    data = input()
    day, hour, minute, rid = map(int, data[:4])
    event = data[4]
    if event == 'A':
        eventType = 0
    elif event == 'C' or event == 'S':
        eventType = 1
    elif event == 'B':
        continue

    hour = day * 24 + hour
    minute = hour * 60 + minute
    if rid not in eventsById:
        eventsById[rid] = []
    eventsById[rid].append((minute, eventType))

for rid in sorted(eventsById):
    eventsById[rid].sort()
    ans = 0
    for event in eventsById[rid]:
        if event[1] == 0:
            prevTime = event[0]
        elif event[1] == 1:
            ans += event[0] - prevTime

    print(ans, end=' ')













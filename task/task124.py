m, n = map(int, input().split())

traffic_lights = dict()

for i in range(1, m+1):
    traffic_lights[i] = 0

for _ in range(n):
    digit_one, digit_two = map(int, input().split())

    traffic_lights[digit_one] = traffic_lights.get(digit_one, 0) + 1
    traffic_lights[digit_two] = traffic_lights.get(digit_two, 0) + 1

traffic_lights_list = list(traffic_lights.items())
# print(traffic_lights_list)
traffic_lights_list.sort()
for i, answer in traffic_lights_list:
    print(answer, end=" ")






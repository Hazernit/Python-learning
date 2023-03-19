x1,	y1,	x2,	y2,	x3,	y3 = map(int, input().split())


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


first_line_dist = distance(x1, y1, x2, y2)
second_line_dist = distance(x2, y2, x3, y3)

polyline_length = first_line_dist + second_line_dist
print(round(polyline_length, 2))







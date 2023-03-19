import math


def find_x_in_2d():
    y1 = int(input())
    x2, y2 = map(int, input().split())
    d = int(input())
    # d - (y1-y2)**2 = (x1-x2) **2
    x1 = (d - (y1 - y2)**2)**0.5 + x2
    print(x1)

def coordinates():
    print("coordinates")
    x1, y1 = map(int, input("Введите координаты х1, y1: ").split())
    x2, y2 = map(int, input("Введите координаты х2, y2: ").split())

    d = ((x1-x2)**2 + (y1-y2)**2)
    d_exact = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print(f"√{d}")
    print(d_exact)

def planes():
    coords = input("Введите координаты в формате x.x, y.y  ... ").split(",")
    x = float(coords[0])
    y = float(coords[1])

    if x < 0.0:
        if y < 0.0:
            print("Третий квадрант")
        elif y > 0.0:
            print("Второй квадрант")
        else:
            print("На x оси")

    elif x > 0.0:
        if y > 0.0:
            print("Первый квадрант")
        elif y < 0.0:
            print("Четвертый квадрант")
        else:
            print("На x оси")

    else:
        if y == 0:
            print("Нулевые координаты")
        else:
            print("На y оси")

def answer_in_3d():
    print("Функция: answer_in_3d()")
    x1, y1, z1 = map(int, input().split())
    x2, y2, z2 = map(int, input().split())
    x2, y2, z2 = x2**0.5, y2**0.5, z2**0.5
    d = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
    print(d)

def coordinates_p_e():
    print("coordinates")
    x1, y1 = math.pi, math.e
    x2, y2 = map(int, input("Введите координаты х2, y2: ").split())

    d = ((x1-x2)**2 + (y1-y2)**2)
    d_exact = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print(f"√{d}")
    print(d_exact)

# find_x_in_2d() # Какое d передать?
# coordinates_p_e()
answer_in_3d()
# find_x_in_2d() # 13

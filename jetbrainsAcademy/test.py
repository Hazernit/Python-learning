import time

import numpy as np

number_one = int(input())
number_two = int(input())
number_free = int(input())

array = np.array([number_one, number_two, number_free])
print(array.max())
print(array.argmax())

help('time.asctime')
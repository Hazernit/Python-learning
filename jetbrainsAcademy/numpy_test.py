import numpy as np

array = np.array([[[14, 5], [8, 0]],
                  [[13, 7], [18, 5]]])
print(array.sum(axis=0))  # вниз [[14+13], [5+7]], [[8+18], [0+5]]  z
print()
print(array.sum(axis=1))  # вправо [[14+8], [5+0]], [[13+18], [7+5]]  y
print()
print(array.sum(axis=2))  # в строку внутри [[14+5], [8+0]], [[13+7], [18+5]]  x

array2 = np.array([[3, 4, 0], [3, 4, 5], [3, 4, 5]])
print(array2.sum(axis=1))
print(array2.prod(axis=1))

array = np.array([7, 80, 15])
print(array.argmax())

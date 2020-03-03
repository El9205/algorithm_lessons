'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''
import random

MIN = 1
MAX = 100
SIZE = 10
list = [random.randint(MIN, MAX) for _ in range(SIZE)]
n_max = 0
n_min = 0
print(list)

for i in range(SIZE):
    if list[i] < list[n_min]:
        n_min = i
    elif list[i] > list[n_max]:
        n_max = i
print('list[%d]=%d list[%d]=%d' % (n_min + 1, list[n_min], n_max + 1, list[n_max]))
b = list[n_min]
list[n_min] = list[n_max]
list[n_max] = b
print(list)

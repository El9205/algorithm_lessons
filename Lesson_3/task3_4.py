# Определить, какое число в массиве встречается чаще всего.

import random

MIN = 1
MAX = 100
SIZE = 10
list = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(list)

num = list[0]
n = 1
for i in range(SIZE - 1):
    a = 1
    for j in range(i + 1, SIZE):
        if list[i] == list[j]:
            a = a + 1
    if a > n:
        n = a
        num = list[i]

if n > 1:
    print(n, num)
else:
    print('Нет повторяющихся элементов')

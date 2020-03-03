'''В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random'''

MIN = -1001
MAX = 100
SIZE = 10
list = [random.randint(MIN, MAX) for _ in range(SIZE)]
n_max = 0
n_min = 0
print(list)

i = 0
index = -1
while i < SIZE:
    if list[i] < 0 and index == -1:
        index = i
    elif list[i] < 0 and list[i] > list[index]:
        index = i
    i += 1

print(index + 1, ':', list[index])

'''Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа'''
import random

MIN = 1
MAX = 100
SIZE = 10
list = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(list)
answer = []
for i in list:
    if i % 2 == 0:
        answer.append(list.index(i))
print(answer)

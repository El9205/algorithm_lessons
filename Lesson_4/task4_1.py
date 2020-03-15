
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile

# вариант 1

def my_rec(n, a=1, sum=0):
    if n == 0:
        return sum
    else:
        return my_rec(n - 1, a / -2, (sum + (a)))
    return sum

print(timeit.timeit('my_rec(5)', number=100, globals=globals())) #0.00042700000000000377
print(timeit.timeit('my_rec(10)', number=100, globals=globals())) #0.0005070999999999964
print(timeit.timeit('my_rec(20)', number=100, globals=globals())) #0.0012999999999999956
print(timeit.timeit('my_rec(40)', number=100, globals=globals())) #0.0029789999999999955
print(timeit.timeit('my_rec(80)', number=100, globals=globals())) #0.004446899999999997

cProfile.run('my_rec(5)') #6/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('my_rec(10)') #11/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('my_rec(20)') #21/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('my_rec(40)') #41/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('my_rec(80)') #81/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)

# Вариант 2
def version_2 (n):
    sum = 1
    c = 1
    for i in range (1, n):
        sum = sum + (c / -2)
        c = c / -2

    return sum

print(timeit.timeit('version_2 (5)', number=100, globals=globals())) #0.00016410000000000036
print(timeit.timeit('version_2 (10)', number=100, globals=globals())) #0.0002634000000000039
print(timeit.timeit('version_2 (20)', number=100, globals=globals())) #0.00047559999999999963
print(timeit.timeit('version_2 (40)', number=100, globals=globals())) #0.0008965999999999974
print(timeit.timeit('version_2 (80)', number=100, globals=globals())) #0.001952300000000004

cProfile.run('version_2 (5)') #1    0.000    0.000    0.000    0.000 task4_1.py:27(version_2)
cProfile.run('version_2 (10)') #1    0.000    0.000    0.000    0.000 task4_1.py:27(version_2)
cProfile.run('version_2 (20)') #1    0.000    0.000    0.000    0.000 task4_1.py:27(version_2)
cProfile.run('version_2 (40)') #1    0.000    0.000    0.000    0.000 task4_1.py:27(version_2)
cProfile.run('version_2 (80)') #1    0.000    0.000    0.000    0.000 task4_1.py:27(version_2)

# Вариант 3

def version_3 (n):
    list = [1]
    c = 1
    for i in range (1, n):
        c = c/-2
        list.append(c)
    return sum(list)

print(timeit.timeit('version_3(5)', number=100, globals=globals())) #0.00019430000000000142
print(timeit.timeit('version_3(10)', number=100, globals=globals())) #0.0002997999999999959
print(timeit.timeit('version_3(20)', number=100, globals=globals())) #0.0006294000000000022
print(timeit.timeit('version_3(40)', number=100, globals=globals())) #0.0017601000000000006
print(timeit.timeit('version_3(80)', number=100, globals=globals())) #0.002246999999999999

cProfile.run('version_3(5)') #6/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('version_3(10)') #11/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('version_3(20)') #21/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('version_3(40)') #41/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)
cProfile.run('version_3(80)') #81/1    0.000    0.000    0.000    0.000 task4_1.py:7(my_rec)


''' Передовалось значение n = 5, 10, 20, 40, 80
Количество измерений - 100, на каждое значение n.
По полученным данным видно, что время выполнения алгоритма возрастает линейно. 
Время выполнения Варианта_2, и Варианта_3 с применением цикла меньше чем у Варианта_1 с применением рекурсии.
В Варианте_2 и Варианте_3, цикл проходит по значения 1 только один раз, но в Варианте_3 тратиться время на добавления элемента в список.
Считаю, что самым оптимальным является код Варианта_3
'''
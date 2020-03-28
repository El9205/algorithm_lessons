'''Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.'''

import hashlib


def some_name(my_string):
    n = 1
    hash_list = []
    for i in range(len(my_string)):
        hash_list.append(hashlib.sha1(my_string[i].encode('utf-8')).hexdigest())
    hash_list = set(hash_list)
    return len(hash_list)


a = some_name('Hello')
print(a)

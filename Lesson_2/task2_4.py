 # https://drive.google.com/file/d/1S8RC9i3qXOeESwE3j26j0ijBZxGxZWWY/view?usp=sharing
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

def my_rec(n, a=1, sum=0):
    if n == 0:
        return sum
    else:
        return my_rec(n - 1, a / -2, (sum + (a)))


x = my_rec(4)
print(x)

#https://drive.google.com/file/d/1BCVb8crNt8K6Z-mow8uBXMj1uo-G5ry1/view?usp=sharing
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int (input('Введите число a: '))
b = int (input('Введите число b: '))
c = int (input('Введите число c: '))

if b<a<c or c<a<b:
    print (a)
elif a<b<c or c<b<a:
    print (b)
else:
    print (c)
# https://drive.google.com/file/d/1rNBjCfIebM1V2tFALqzYf1UY12JX-4D4/view?usp=sharing
#Определить, является ли год, который ввел пользователь, високосным или не високосным.

a = int(input('Введите год: '))

if a % 4 == 0:
    print ("Год високосный")
else:
    print ('Год не високосный')
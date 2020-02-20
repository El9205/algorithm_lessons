#https://drive.google.com/file/d/1Zh36zz7SWVgzjBdHGVSONWWr6W02wOxI/view?usp=sharing
#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите число от 100 до 999: '))

a = number // 100
b = (number % 100) // 10
c = number % 10

print (a+b+c)
print (a*b*c)

#https://drive.google.com/file/d/1hcwZyJ5nQ-11UOYH-rEspurgoFsHimB0/view?usp=sharing
'''3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.'''

num = input('Введите число: ')
a = ''
for i in num:
    a = i + a
print(a)

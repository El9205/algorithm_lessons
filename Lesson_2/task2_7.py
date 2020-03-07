 #https://drive.google.com/file/d/1V98vkdP_Xwr4prKRwwkgpjwAxrqpZVgB/view?usp=sharing
'''7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n — любое натуральное число.'''

n = int(input('Введите натуральное число: '))
sum1 = 0
sum2 = n * (n + 1) // 2
for i in range(1, n+1):
    sum1 = sum1 + i

print(sum1)
print(sum2)
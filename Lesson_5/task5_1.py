'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.'''

from collections import defaultdict

mid_prof = 0
n = int(input("Введите количество предприятий: "))
company=[]
for i in range(n):
    name = input('Введите название предприятия: ')
    for j in range(4):
        profit = int(input('Введите прибыль за 4 квартала: '))
        company.append((name, profit))

all_companies = defaultdict(list)
for name, profit in company:
    all_companies[name].append(profit)
print(all_companies)
for c in all_companies:
    all_companies[c] = sum(all_companies[c])/4
    mid_prof += all_companies[c]
mid_prof = int(mid_prof/n)
print (all_companies)


for q in all_companies:
    if all_companies[q] >= mid_prof:
        print('Прибыль предприятия ' + q + ' равно или выше среднего')
    else:
        print('Прибыль предприятия ' + q + ' ниже среднего')



# Автоматизація опрацювання елементів кортежів за допомогою циклів
'''
Задача:
Оператору компанії необхідно вивести кожне
значення заборгованостей по оплаті за газ в окремому рядку.
Розв'язок задачі:
В циклі для змінної element, що набуває значення кожного елементу кортежу, по черзі:
вивести значення element на екран
'''

gas_volume = (153, 220, 0)

for element in gas_volume:
    print(element)

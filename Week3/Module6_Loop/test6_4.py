'''
Реалізувати програму, яка обчислює і виводить на екран суму всіх чисел від 1 до введеного користувачем числа включно.

Додаткові умови:

Використати цикл while або for;
Результат роботи програми - ціле число;
Введене користувачем число зберігається в змінній number.
'''

number = int(input("Введіть число"))
sum = 0

for i in range(1, number + 1):
    sum = sum + i

print(sum)
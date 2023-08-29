'''
Реалізувати функцію, яка виводить на екран значення від 0 до заданого числа включно з кроком 2.

Додаткові умови:
Функція має мати ім’я print_numbers;
Функція має один параметр - ціле число;
Результат роботи функції - послідовність чисел від 0 до заданого числа включно з кроком 2
Кожне число має бути в новому рядку;
Функція має містити в собі директиву print.
Очікуваний результат виконання програми:

Для набору вхідних даних (4) – функція виводить на екран
0
2
4
Для набору вхідних даних (7) – функція виводить на екран
0
2
4
6
'''

def print_numbers(number):
    for i in range(0, number + 1, 2):
        print(i)
    

number = int(input("Введіть число "))
print_numbers(number)
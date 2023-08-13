'''
Реалізувати функцію, яка визначає чи число парне чи непарне.

Додаткові умови:
Функція має мати ім’я is_even_or_odd;
Функція має один параметр - ціле число;
Результат роботи функції - текст “число n парне” або “число n непарне”, де n - число яке ввів користувач;
Функція не має містити в собі директиву print
Очікуваний результат виконання програми:

Для набору вхідних даних (2) – функція повертає – “число 2 парне”
Для набору вхідних даних (3) – функція повертає – “число 3 непарне”
'''

def is_even_or_odd(number):
    if number % 2 == 0:
        return f"число {number} парне"
    else:
        return f"число {number} непарне"



number = int(input("Введіть число"))
print(is_even_or_odd(number))
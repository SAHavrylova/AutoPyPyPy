'''
Написати програму, яка створює кортеж numbers1 з п'яти елементів, введених користувачем, створює новий кортеж numbers2 з двох останніх елементів кортежу numbers1 і виводить на екран кортеж numbers2.

Додаткові умови:
Введені користувачем значення зберігаються в змінних value1, value2, value3, value4, value5;
Використовувати функцію print лише для виводу результату задачі.
Очікуваний результат виконання програми:

Для набору даних ('1', '2', '3', '4', '5') – текст на екрані – ('4', '5')
Для набору даних ('Ukraine', 'Poland', 'US', 'Austria', 'Great Britain') – текст на екрані – ('Austria', 'Great Britain')
'''

value1 = input("Введіть перший елемент ")
value2 = input("Введіть другий елемент ")
value3 = input("Введіть третій елемент ")
value4 = input("Введіть четвертий елемент ")
value5 = input("Введіть п'ятий елемент ")

numbers1 = (value1, value2, value3, value4, value5)
numbers2 = (value4, value5)

print(numbers2)
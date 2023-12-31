'''
Написати програму, що перетворить введені прізвище, ім'я, по батькові (три окремі рядкові величини) у прізвище та ініціали та вивести цей рядок на екран.

Додаткові умови:
Не виводити додаткові символи в функції print окрім очікуваних;
Можливі значення введеного користувачем прізвища - рядковий тип даних;
Можливі значення введеного користувачем імені - рядковий тип даних;
Можливі значення введеного користувачем по батькові - рядковий тип даних;
Якщо користувач ввів пустий рядок в будь-яку з вхідних змінних - вивести повідомлення "Не введений ключовий параметр";
Використовувати функцію print лише для виводу результату задачі;
Використати метод len;
Обов'язково використати функцію форматування рядків format()
Очікуваний результат виконання програми:

Для набору даних (Бандера, Степан, Андрійович) – текст на екрані – Бандера С.А.
Для набору даних (Бандера, Степан, "" ) – текст на екрані – Не введений ключовий параметр
Для набору даних ("", Степан, Андрійович ) – текст на екрані – Не введений ключовий параметр

'''

last_name = input("Введіть прізвище ")
name = input("Введіть ім'я ")
second_name = input("Введіть по батькові ")

if len(last_name) == 0  or len(second_name) == 0 or len(name) == 0:
    print("Не введений ключовий параметр")
else:
    print("{0} {1}.{2}.".format(last_name, name[0], second_name[0]))
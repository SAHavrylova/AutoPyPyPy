'''
Створити програму, яка перевіряє чи є введене користувачем число в списку [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Додаткові умови:
Введене користувачем цілочисельне значення зберігається в змінній number;
Якщо число існує - вивести на екран "Введене число - існує"
Якщо числа не існує - вивести на екран "Введене число - не існує"
Використовувати функцію print лише для виводу результату задачі.
Функція print не має містити нічого зайвого, крім очікуваного результату
Перевірку виконати використовуючи цикл for і розгалуження if
Очікуваний результат виконання програми:

Для набору даних (1) – текст на екрані – "Введене число - існує".
Для набору даних (11) – текст на екрані – "Введене число - не існує".
'''

number = int(input("Введіть число "))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

for i in a:
    if i == number:
        print("Введене число - існує")
    else:
        print("Введене число - не існує")

number = int(input("Введіть число: "))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number_found = False  # Ініціалізуємо змінну, що вказує, чи знайдено число

for i in a:
    if i == number:
        number_found = True

if number_found:
    print("Введене число - існує")
else:
    print("Введене число - не існує")

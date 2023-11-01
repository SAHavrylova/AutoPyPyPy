'''
Напишіть функцію max_two, яка визначає більше з двох чисел a, b. Використовуючи цю
функцію, знайдіть найбільше з чотирьох чисел.
Пояснення розв’язку
Опишемо допоміжний алгоритм, який називається max_two. Нехай вхідними
параметрами будуть a, b. В тілі допоміжного алгоритму використаємо
розгалуження з умовою a>b. Якщо умова виконується то змінній max присвоюємо
значення a, в іншому випадку max присвоюємо значення b. Значення max
повертатиметься в головний алгоритм.
Організовуємо у головній програмі введення 4 чисел, відповідно у змінні number1,
number2, number3, number4. Викликаємо допоміжний алгоритм max_two з
параметрами number1, number2 та повертаємо значення у змінну
more_than_two1. Повторно викликаємо допоміжний алгоритм max_two з
параметрами number3, number4 та повертаємо значення у змінну
more_than_two2. Втретє викликаємо допоміжний алгоритм max_two з
параметрами more_than_two1, more_than_two2 та повертаємо значення у
змінну more_than_four. Виводимо змінну more_than_four на екран.
'''

def max_two(a, b):
    if a > b:
        max = a
    else:
        max = b
    return max

number1 = float(input("number1 ="))
number2 = float(input("number2 ="))
number3 = float(input("number3 ="))
number4 = float(input("number4 ="))
more_than_two1 = max_two(number1, number2)
more_than_two2 = max_two(number3, number4)
more_than_four = max_two(more_than_two1, more_than_two2)

print(more_than_four)
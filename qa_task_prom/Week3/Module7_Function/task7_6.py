'''
Напишіть функцію, яка перевіряє, чи існує трикутник із введеними сторонами a, b, c.
Пояснення розв’язку
Трикутник існує, якщо сума довжин будь-яких двох його сторін більша за довжину
третьої сторони.
Опишемо допоміжний алгоритм, який назвемо triangle_check. Нехай вхідними
параметрами будуть side1, side2 та side3. В тілі алгоритму використовуємо
розгалуження з умовою side1> = side2 + side3, якщо умова істинна то змінній
rez присвоюємо значення “False”, у іншому випадку змінній rez присвоюємо“True”.
Організовуємо у головній програмі введення трьох чисел a, b, c. Викликаємо
допоміжний алгоритм triangle_check з параметрами a, b, c, а результат
виконання присвоюємо змінній rez1. Повторно викликаємо допоміжний алгоритм
triangle_check, але вже з параметрами b, a, c, а результат виконання
присвоюємо змінній rez2. І втретє викликаємо допоміжний алгоритм
triangle_check, але вже з параметрами c, b, a, а результат виконання
присвоюємо змінній rez3. Організовуємо вивід (rez1 and rez2 and rez3), якщо
жодна із змінних rez1, rez2, rez3, не матиме значення “False”, то результат на
екрані буде “True”, інакше на екрані буде виведено “False”.
'''

def triangle_check(side1, side2, side3):
    if side1 >= side2 + side3:
        return False
    else:
        return True
    

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

rez1 = triangle_check(a, b, c)
rez2 = triangle_check(b, a, c)
rez3 = triangle_check(c, b, a)

if rez1 and rez2 and rez3:
    print("True")
else:
    print("False")    



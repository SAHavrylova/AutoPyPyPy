'''
Відомі дві швидкості: одна задана в кілометрах за годину, інша - в метрах за секунду. Яка з швидкостей більша?
Пояснення розв’язку
Вводимо два числа: швидкість в кілометрах за годину speed1 і швидкість в метрах за секунду speed2. Перед порівнянням переведемо speed1 в метри за секунду. Для цього використаємо формулу speed1 = speed1*1000/3600(так як 1 км = 1000 м і 1год. = 3600 с ). Далі порівнюємо вже змінене значення speed1 зі speed2. Якщо speed1>speed2 змінній res присвоюємо значення “First speed is higher”, інакше перевіряємо умову speed1<speed2. Якщо ця умова виконується, то res присвоюємо значення “Second speed is higher”, інакше res присвоюємо значення “Speeds are the same”. Виводимо res на екран.
'''

speed1 = float(input("speed1 ="))
speed2 = float(input("speed2 ="))
speed1 = speed1 * 1000 / 3600

if speed1 > speed2:
    res = "First speed is higher"
else:
    if speed1 < speed2:
        res = "Second speed is higher"
    else:
        res = "Speeds are the same"

print(res)
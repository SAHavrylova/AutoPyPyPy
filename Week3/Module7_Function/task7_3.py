'''
Дано чотири числа x1, y1, x2, y2. Написати функцію dist(x1, y1, x2, y2), яка обчислює
відстань між двома точками (x1, y1) та (x2, y2).
Пояснення розв’язку
Опишемо допоміжний алгоритм, який назвемо dist. Нехай
вхідними параметрами будуть x1, y1, x2, y2. В тілі
алгоритму обчислюємо значення змінної distance за
формулою math.sqrt((x1-x2)*(x1-x2) +
(y1-y2)*(y1-y2)). Це значення і повертатиметься в
головний алгоритм.
Організовуємо у головній програмі введення 4 чисел,
відповідно у змінні coordx1, coordy1 (для першої
точки), coordx2, coordy2 (для другої точки).
Викликаємо допоміжний алгоритм dist з параметрами
coordx1, coordy1, coordx2, coordy2 та
повертаємо значення у змінну
distance_between_points. Виводимо змінну distance between points на
екран.
'''

import math

def dist(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print(distance)


coordx1 = float(input("x1 ="))
coordy1 = float(input("y1 ="))
coordx2 = float(input("x2 ="))
coordy2 = float(input("y2 ="))
distance_between_points = dist(coordx1, coordy1, coordx2, coordy2)

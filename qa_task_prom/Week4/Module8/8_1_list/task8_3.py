'''
Створити список , який складатиметься з 9 значень цілого типу. Організувати введення
цього списку з клавіатури. Знайти кількість від’ємних елементів списку
Пояснення розв’язку
Оголошуємо список mas.
Організовуємо цикл з параметром i, де і буде змінюватися від 0 до 8 з кроком 1. В
тілі циклу організовуємо введення значення цілого типу у змінну el. Значення змінної
el заносимо в список mas.
Оголошуємо змінну count для знаходження кількості від'ємних елементів та
присвоюємо їй значення 0.
Повторно використовуємо цикл з параметром i. В циклі перевіряємо чи чергове
значення списку mas від'ємне, якщо так, то збільшуємо значення змінної count на
1.
Виводимо значення count на екран.
'''

mas = []

for i in range(9):
    el = int(input("el ="))
    mas.append(el)

count = 0

for i in range(9):
    if mas [i] < 0:
        count = count + 1

print(count)
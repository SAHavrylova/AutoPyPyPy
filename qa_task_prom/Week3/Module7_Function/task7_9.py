'''
Вкладник розмістив суму розміром n грн. в банку. Визначте, яку суму отримає вкладник
через m років, якщо відсоткова ставка складає p% в рік. Дані вводяться в порядку n, p,
m як у вхідних даних.
Пояснення розв’язку
Опишемо допоміжний алгоритм, який назвемо deposit. Нехай вхідними
параметрами будуть dep, rate та year. В тілі алгоритму використовуємо змінну
suma для обчислення суми яка буде через певну кількість років за формулою: dep +
dep*rate/100*year.
Організовуємо у головній програмі введення 3 числа n, p, m. Викликаємо
допоміжний алгоритм deposit з параметрами n, p, m, а результат записуємо у
змінну result. Виводимо значення result на екран.
'''

def deposit(dep, rate, year):
    suma = dep + dep * rate / 100 * year
    return suma


n = float(input("n ="))
p = float(input("p ="))
m = float(input("m ="))

result = deposit(n, p, m)

print(result)
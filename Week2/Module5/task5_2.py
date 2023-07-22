'''
Напишіть програму яка перевіряє, чи є введене число додатним, від’ємним або це нуль.
Пояснення розв’язку
Вводимо число number. Порівнюємо його з нулем. Якщо number > 0, то res присвоюємо “Number is positive”. Далі перевіряємо чи number < 0, якщо так, то res присвоюємо “Number is negative”. Далі перевіряємо чи number == 0, якщо так, то res присвоюємо “Number is zero”. Виводимо значення змінної res.
'''
number = float(input("number= "))

if number > 0:
    res = "Number is positive"

if number < 0:
    res = "Number is negative"

if number == 0:
    res = "Number is zero"

print(res)
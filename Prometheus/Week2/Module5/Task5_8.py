'''
Напишіть програму, яка запитує два цілих числа. Якщо добуток чисел перевищує їх суму, надрукувати добуток чисел, у протилежному випадку - вивести їх суму. Якщо ж добуток дорівнює сумі, вивести різницю чисел.
Пояснення розв’язку
Ввести два числа num1 та num2. Знаходимо їх суму та записуємо в комірку sum. Знаходимо їх добуток та записуємо в комірку product. Порівнюємо sum<product, якщо так, то res присвоюємо product. Якщо sum>product, то res присвоюємо значення sum. У випадку рівності sum і product, res присвоюємо num1-num2. Виводимо res.
'''

num1 = float(input("num1 ="))
num2 = float(input("num2 ="))
sum = num1 + num2
product = num1 * num2

if sum < product:
    res = product
else:
    if sum > product:
        res = sum
    else:
        res = num1 - num2

print(res)

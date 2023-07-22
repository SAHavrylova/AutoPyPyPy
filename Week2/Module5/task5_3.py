'''
Напишіть програму, на вхід якої подається два цілих числа - вік Сашка і вік Тетянки. Програма має вивести повідомлення про те, хто є старшим серед них.
Пояснення розв’язку
Вводимо два цілих числа age_Sasha та age_Tanya. Порівнюємо їх. Якщо виявиться, що age_Sasha > age_Tanya, то змінній res присвоюємо “Sasha is older”. Далі перевіряємо чи age_Sasha < age_Tanya. Якщо ж age_Sasha < age_Tanya, res присвоюємо “Tanya is older”. У випадку, якщо жодна вимога не виконується, це означає, що вік обидвох однаковий, а отже res присвоюємо “Sasha and Tanya are the same age”.
'''

age_Sasha = int(input("age_Sasha ="))
age_Tanya = int(input("age_Tanya ="))

if age_Sasha > age_Tanya:
    res = "Sasha is older"

elif age_Sasha < age_Tanya:
    res = "Tanya is older"
else:
    res = "Sasha and Tanya are the same age"

print(res)
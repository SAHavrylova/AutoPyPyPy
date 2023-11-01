'''
Скласти програму, яка аналізує введений користувачем текст. Якщо у тексті є російські літери "ы", "ъ", "ё", "э", то у відповідь виводиться повідомлення "Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!", у протилежному випадку на екран виводиться повідомлення "Дякуємо за замовлення!"

Додаткові умови:
Не виводити додаткові символи в функції print окрім очікуваних;
Можливі значення введених користувачем рядків - рядковий тип даних;
Використовувати функцію print лише для виводу результату задачі.
Очікуваний результат виконання програми:

Для набору даних ("Добрый день!") – текст на екрані – "Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!"
Для набору даних ("Доброго вечора! Ми з України!") – текст на екрані – "Дякуємо за замовлення!"
'''

text = input("Write a text: ")

if "ы" in text or "ъ" in text or "ё" in text or "э" in text:
    print("Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!")
else:
    print("Дякуємо за замовлення!")

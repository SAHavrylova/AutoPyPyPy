'''
Скласти програму для повідомлення користувача про низький заряд батареї телефона за допомогою короткої форми вказівки розгалуження. Вважати пороговим значенням заряду, що вважається низьким - від 0% до 15% включно Результатом виконання задачі є виведене на екран повідомлення користувачу про низький заряд телефона

Додаткові умови

Вхідні дані вводяться з клавіатури користувачем
Можливе значення відсотків заряду телефона - додатне дійсне число
Використовувати функцію print лише один раз для виводу результату задачу
Очікуваний результат виконання програми:

Для набору даних (battery_power = 20.5) – текст на екрані відсутній
Для набору даних (battery_power = 11) – текст на екрані - “Заряд телефону низький”
'''

battery_power = float(input("power ="))

if 0 <= battery_power <= 15:
    print("Заряд телефону низький")
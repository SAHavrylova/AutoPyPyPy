'''
Скласти програму для визначення кількості бандеромобілів, які зможуть придбати волонтери за донати українців. Відома вартість одного Бандеромобіля - 6500 євро, курс євро до гривні (вводиться користувачем) та сума в гривнях, яку зібрали волонтери (вводиться користувачем). Результатом виконання програми є ціле додатне число, яке дорівнює кількості бандеромобілів.

Додаткові умови

Можливі значення курсу гривні до євро - додатне дійсне число;
Можливі значення суми, яку зібрали волонтери - додатне ціле число;
Використовувати функцію print лише один раз для виводу результату задачі.
Підказка:
Для визначення кількості бандеромобілів скористайтеся операцією ділення націло.

Очікуваний результат виконання програми:

Для набору вхідних даних (курс = 39,5, сума = 2500000) – результат на екрані – 9
'''

course = float(input("c ="))
sum = int(input("s ="))
euro = 6500
total_euro = sum / course
result = int(total_euro / euro)

print(result)
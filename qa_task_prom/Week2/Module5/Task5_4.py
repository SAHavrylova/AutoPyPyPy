'''
Підприємство набирає робітників у штат. Умова прийому потребує не менше 5 років робочого стажу та вік не більше 40 років. Створіть програму, яка перевіряє, підходить кандидатура по цим параметрам чи ні.
Пояснення розв’язку
Вводимо стаж робітника experience та його вік age. Виконуємо порівняння experience>=5 і одночасно чи age<=40 (для цього використовуємо логічну операцію “і”), якщо обидві умови виконуються одночасно то змінній rez присвоюємо “Candidate is suitable”, інакше присвоюємо їй “Candidacy is not suitable”
'''

experience = float(input("expirience ="))
age = float(input("age ="))

if experience >= 5 and age <= 40:
    rez = "Candidate is suitable"
else:
    rez = "Candidacy is not suitable"

print(rez)

# Доступ до елементів рядка

str1 = "Слава Україні!"
number = int(input("Введіть номер символу для перевірки. Номер має бути від 0 та не більше 13"))

while number < 0 or number > 13:
    print("Введіть правильний порядковий номер")
    number = int(input("Введіть номер символу для перевірки. Номер має бути від 0 та не більше 13"))

if str1[number] == "!":
    print("Символ з індексом", number, "є знаком оклику(!)")
else:
    print("Символ з індексом", number, "не є знаком оклику(!)")
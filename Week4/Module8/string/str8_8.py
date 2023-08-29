# Опрацювання рядків - отримання довжини рядка

str1 = input("введіть словосполучення для його подальшого опрацювання ")
max_index = len(str1) - 1

input_msg = f"Введіть номер символу для перевірки. Номер має бути від 0 та не більше {max_index} "
number = int(input(input_msg))

while number < 0 or number > max_index:
    print("Введіть правильний порядковий номер")
    number = int(input(input_msg))

if str1[number] == "!":
    print("Символ з індексом", number, "є знаком оклику(!)")
else:
    print("Символ з індексом", number, "не є знаком оклику(!)")
# Опрацювання рядків - отримання довжини рядка

str1 = input("введіть словосполучення для його подальшого опрацювання ")
str1_lenght = len(str1)

print(f"Кількіст символів у рядку '{str1}' = {str1_lenght}")
print(f"Перший символ = {str1[0]}")
print(f"Останній символ = {str1[len(str1) - 1]}")
#Опрацювання рядків - перевірка наявності символів

str1 = "Слава Україні!"
ch = input("Слово чи символ для перевірки наявності ")

if ch in str1:
    print(f"Символ або слово {ch} присутній у рядку {str1}")
else:
    print(f"Символ або слово {ch} відсутній у рядку {str1}")
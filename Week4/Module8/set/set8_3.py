#Вилучення елементів множини

countries = {"Ukraine", "Poland", "Сhina"}
print(countries)

uk = "Great Britain"
countries.add(uk)
print(countries)

countries.remove("Сhina")
countries.discard("Austria")
print(countries)
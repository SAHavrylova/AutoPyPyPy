'''
Задача:
Оператору компанії необхідно ввести значення
заборгованостей по оплаті за газ.
Розв'язок задачі:
1. Кількість споживачів газу N=5
2. Створення списку gas_cost
3. В циклі для і, що змінюється від 0 до N-1 з кроком 1:
Ввести gas_arrears для споживача з номером і
Додати це значення до списку gas_cost 
''' 

# Автоматизація заповнення списку 

N = 5
gas_cost = []

for i in range(N):
    gas_arrears = float(input("fill ="))
    gas_cost.append(round(gas_arrears, 2))

print(gas_cost)    
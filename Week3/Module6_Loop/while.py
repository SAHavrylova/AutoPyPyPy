deposit_amount = float(input("deposit_amount ="))
annual_rate = float(input("annual_rate ="))
desired_amount = float(input("desired_amount ="))

deposit_period = 0

while deposit_amount < desired_amount:
    deposit_period = deposit_period + 1
    deposit_amount = deposit_amount + deposit_amount * annual_rate / 100

print("Очікуваний термін депозиту =", deposit_period, "років")
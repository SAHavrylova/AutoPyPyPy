count = float(input("count= "))
tariff = 7.80
price = tariff * count

print("Price light= ", round(price, 2))

cash = float(input("cash= "))
if cash >= price:
    rest = cash - price
    print("Rest= ", round(rest, 2))
else:
     print("Low cash")


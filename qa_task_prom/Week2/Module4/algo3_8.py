import math

cost = int(input("cost ="))
period = int(input("period ="))
total_cost = math.floor(365 / period) * cost

print(total_cost)
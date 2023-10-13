class ShopWorker:
    pass
worker_one = ShopWorker()
worker_two = ShopWorker()
print(worker_one)
print(worker_two)

worker_one.name = "Dima"
worker_one.age = 37

worker_two.name = "Sveta"
worker_two.age = 35

print("User 1: ",worker_one.name," ", worker_one.age)
print("User 1: ",worker_two.name," ", worker_two.age)
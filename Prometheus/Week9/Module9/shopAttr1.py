class ShopWorker:
    count_workers = 2

worker_one = ShopWorker()
worker_two = ShopWorker()

worker_one.name = "Dima"
worker_one.age = 37

worker_two.name = "Sveta"
worker_two.age = 35

print("User 1: ",worker_one.name," ", worker_one.age, 
      " all workers ", worker_one.count_workers)
print("User 2: ",worker_two.name," ", worker_two.age,
      " all workers ", worker_two.count_workers)
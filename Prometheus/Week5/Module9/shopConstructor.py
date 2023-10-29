class ShopWorker:
    count_workers = 0
    def __init__(self):
        ShopWorker.count_workers +=1

print("all users ", ShopWorker.count_workers)

worker_one = ShopWorker()
worker_one.name = "Dima"
worker_one.age = 37

print("User 1: ",worker_one.name," ", worker_one.age, 
      " all workers ", worker_one.count_workers)

worker_two = ShopWorker()
worker_two.name = "Sveta"
worker_two.age = 35

print("User 2: ",worker_two.name," ", worker_two.age, 
      " all workers ", worker_two.count_workers)
class ShopWorker:
       count_workers = 0
       def __init__(self, name1="", age1=0):
           self.name = name1
           self.age = age1
           ShopWorker.count_workers +=1

print("all users ", ShopWorker.count_workers)

worker_one = ShopWorker()

print("User 1: ",worker_one.name," ", worker_one.age, 
      " all workers ", worker_one.count_workers)

worker_two = ShopWorker("Dima", 37)

print("User 2: ",worker_two.name," ", worker_two.age, 
      " all workers ", worker_two.count_workers)

worker_three = ShopWorker("Sveta")

print("User 2: ",worker_three.name," ", worker_three.age, 
      " all workers ", worker_three.count_workers)
class ShopWorker:
      count_workers = 0
      def __init__(self, name1="", age1=0):
           self.name = name1
           self.age = age1
           ShopWorker.count_workers +=1
      def add_year(self):
           self.age +=1

print("all users ", ShopWorker.count_workers)

worker_one = ShopWorker("Dima", 37)

print("User 1: ",worker_one.name," ", worker_one.age, 
      " all workers ", worker_one.count_workers)

worker_one.add_year()

print("User 1: ",worker_one.name," ", worker_one.age, 
      " all workers ", worker_one.count_workers)

worker_two = ShopWorker("Sveta", 35)

print("User 2: ",worker_two.name," ", worker_two.age, 
      " all workers ", worker_two.count_workers)

worker_two.add_year()

print("User 2: ",worker_two.name," ", worker_two.age, 
      " all workers ", worker_two.count_workers)
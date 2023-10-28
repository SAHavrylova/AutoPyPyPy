class ShopWorker:
      count_workers = 0
      def __init__(self, name1="", age1=0):
           self.name = name1
           self.age = age1
           ShopWorker.count_workers +=1
           self.id=ShopWorker.count_workers
      def add_year(self, year):
           self.age +=year
      def __str__(self):
           str_out="Worker"+str(self.id)+": "+self.name+" "+str(self.age)
           str_out += "all workers " + str(ShopWorker.count_workers)
           return str_out
      @staticmethod
      def info():
           print("In a shop work: ", ShopWorker.count_workers, " workers")
      @classmethod
      def naming_shop(cls, name):
           cls.name_shop= name
           return cls.name_shop
ShopWorker.info()
worker_one = ShopWorker("Dima", 37)
print(worker_one)
worker_one.add_year(3)
print(worker_one)
worker_two = ShopWorker("Sveta", 35)
print(worker_two)
worker_two.add_year(2)
print(worker_two)
print("Shop name: ", worker_one.naming_shop("Fara"))
print("Shop name: ", ShopWorker.name_shop)
print("Shop name: ", ShopWorker.naming_shop("Para"))
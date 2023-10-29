# Приклад 1. Успадкування атрибутів
class ShopWorker:
    _count_workers = 0
    def __init__(self, name1="", age1=0):
        self.name = name1
        self._age = age1
        self.setting_id()
    def setting_id(self):
        ShopWorker._count_workers +=1
        self.id = ShopWorker._count_workers
    def add_year(self):
        self._age +=1
    def __str__(self):
        str_out="Worker"+str(self.id)+": "+self.name+" "+str(self._age)
        str_out += " all workers " + str(ShopWorker._count_workers)
        return str_out
    @staticmethod
    def info():
        print("In a shop work: ", ShopWorker._count_workers, " workers")
    @classmethod
    def naming_shop(cls, name):
        cls.name_shop= name
        return cls.name_shop
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        if (new_age < 0):
            new_age = - new_age
        self._age=new_age
class Seller (ShopWorker):
    pass    

ShopWorker.info()

worker_one = ShopWorker("Dima", 37)
print(worker_one)
worker_one.add_year()
print(worker_one)
ShopWorker.naming_shop("Fara")
print("Shop name: ", ShopWorker.name_shop)

seller1= Seller()
print(seller1)
print(seller1.name)
seller2= Seller("Maria", 40)
print(seller2)
print(seller2.name)
print(Seller.name_shop)
print(Seller._count_workers)
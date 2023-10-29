# Приклад 3. Успадкування методів
class ShopWorker:
    _count_workers = 0
    def __init__(self, name1="", age1=0):
        self.name = name1
        self._age = age1
        self.setting_id()
    def setting_id(self):
        ShopWorker._count_workers +=1
        self.id = ShopWorker._count_workers
    def working(self):
        print("Working now")
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
    def __init__(self, name1="", age1=0, cash1=0 ):
        super().__init__(name1, age1)
        self.cash = cash1
    def __str__(self):
        return super().__str__()+ " work with cash "+ str(self.cash)
    def working(self):
        print("Service customer")
class StoreManage (ShopWorker):
    def working(self):
        print("Director")
class ShopCleaner (ShopWorker):
    def working(self):
        print("Cleaner")

worker_one = ShopWorker("Dima", 37)
seller1= Seller("Oksana", 28, 3456.50)
store_manager = StoreManage()
shop_cleaner = ShopCleaner()

worker_one.working()
seller1.working()
store_manager.working()
shop_cleaner.working()
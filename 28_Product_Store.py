class Product:
    count = 0

    def __init__(self,name,price): #we get to know object creation here
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in Store = {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"discounted price = {price - (price * discount /100)}")


p1 = Product("Phone",10_000)
p2 = Product("Laptop",50_000)
p3 = Product("Mac",1_00_000)
p4 = Product("Earphone",500)

p2.get_info()
Product.get_count()
p1.calc_discount(p1.price,10)
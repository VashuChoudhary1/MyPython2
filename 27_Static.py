class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage
    

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"final price = {final_price}")

l1 = Laptop("16gb","512gb")
l1.calc_discount(40_000,10)
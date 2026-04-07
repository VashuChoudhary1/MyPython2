#we also use decorator in class
class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage

    @classmethod #it is decorator that make this function as class method , chng behaviour 
    def get_storage_type(cls):
        print(f"storage type is {cls.storage_type}")

l1= Laptop("16gb","512gb")
print(Laptop.get_storage_type())
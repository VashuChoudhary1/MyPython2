#instance, class and static methods
#INSTANCE METHOD - HAS SELF PARAMTER , IT CAN ACCESS CLASS AS WELL AS INSTANCE ATTRIBUTES
class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage
    
    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.Storage} {self.storage_type}")

l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb","256gb")

l1.get_info()

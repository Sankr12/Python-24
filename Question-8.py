# WRT 7th Question, create 3 laptop objects and add them to the 
# list in the sorted order based on the ram size

class laptop:

    def __init__(self,brand,CPU,RAM,HDD):
        self.brand = brand
        self.CPU = CPU
        self.RAM = RAM
        self.HDD = HDD

    def __repr__(self):
        return f"laptop({self.brand}, RAM: {self.RAM}GB)"


laptop1 = laptop("hp","i7",16,512)
laptop2 = laptop("Dell","i5",8,1024)
laptop3 = laptop("Asus","i9",64,2048)

laptops = [laptop1, laptop2,laptop3]

sorted_laptops = sorted(laptops, key=lambda x: x.RAM)

print(sorted_laptops)
# Write a python program to create a laptop class with 4 attributes 
# (brand,CPU,RAM,HDD) and 2 methods (showconfig() to print the values,
# __init__() to initialize the values)

class laptop:

    def __init__(self,brand,CPU,RAM,HDD):
        self.brand = brand
        self.CPU = CPU
        self.RAM = RAM
        self.HDD = HDD

    def showconfig(self):
        print("Brand:",self.brand,"\nCPU:",self.CPU,"\nRAM:",self.RAM,"\nHDD:",self.HDD)

laptop1 = laptop("hp","i7",16,512)
laptop2 = laptop("Dell","i5",8,1024)
laptop3 = laptop("Asus","i9",64,2048)

laptop1.showconfig()
print()
laptop2.showconfig()
print()
laptop3.showconfig()
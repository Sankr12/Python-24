# Write a python program to create 3 user objects and find the youngest of all

class user:

    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def compare(self,another1,another2):
        if self.age<another1.age and self.age<another2.age:
            print(f"{self.name} is the youngest")
        elif another1.age<self.age and another1.age<another2.age:
            print(f"{another1.name} is the youngest")
        else:
            print(f"{another2.name} is the youngest")

user1 = user("Sandeep", 21, "sandeepskvverma1@gmail.com")
user2 = user("Vikas", 22, "vikasyadav21@gmail.com")
user3 = user("Manish", 23, "manishpurigoswami@gmail.com")

user1.compare(user2)
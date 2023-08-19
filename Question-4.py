# Write a python program to init default values for user object using __init__ method

class user:
    def __init__(self,name="sandeep",age=21,email="sandeepskvverma1@gmail.com"):
        self.name = name
        self.age = age
        self.email = email
    def show(self):
        print("Name:",self.name,"\nAge:",self.age,"\nEmail:",self.email)

user1 = user()
user2 = user()

user1.show()
user2.show()
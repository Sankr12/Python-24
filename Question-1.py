# Write a python program to create a user class with 3 properties : name,age,email

class user:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

user1 = user("Sandeep", 21, "sandeepskvverma1@gmail.com")

print("Name:",user1.name)
print("Age:",user1.age)
print("Email:",user1.email)
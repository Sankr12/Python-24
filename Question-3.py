# Write a python to create 2 objects of the user class and assign different values

class user:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

user1 = user("Sandeep",21,"sandeepskvverma1@gmail.com")
user2 = user("Sanjay",23,"kumars87743@gmail.com")

print("Name:",user1.name)
print("Name:",user2.name)
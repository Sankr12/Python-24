# Write a python program to create a user class with a method to greet the user

class user:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    def greet_user(self):
        print(f"Hello {self.name}! Welcome to our platform")

user1 = user("Sandeep", 21, "sandeepskvverma1@gmail.com")
print()
user1.greet_user()
print()
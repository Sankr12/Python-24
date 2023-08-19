# Write a python progam to delete the age property of the user

class user:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
        
user1 = user("Sandeep",21,"sandeepskvverma1@gmail.com")

del user1.age

if hasattr(user1, 'age'):
    print("Age property still exist")
else:
    print("Age property has been deleted")
# Define a class Employee with instance object variables empid,
# name, salary. Write __init__() method in the class to
# initialize instance object variables. Also define
# instance methods to input fields and display field values

class Employee:

    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    
    def __repr__(self):
        return f"Employ Id: {self.empid} \nName: {self.name} \nSalary: {self.salary}"

Employee1 = Employee(231, "Rachit", 23560)
Employee2 = Employee(563,"Vikas",23541)
Employee3 = Employee(566, "Gaurav", 78657)

print(Employee1)
print(Employee2)
print(Employee3)
# Write a python program to create a school class and 3 instances variables and 1 
# class variable

class school:
    standard = "XI"

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def __repr__(self):
        return f"Name: {self.name}\nRoll no.:{self.rollno}\nMarks: {self.marks}"

Student1 = school("AK Trishant", "00111402020", 82.5)
Student2 = school("Abhishek Yadav", "00211402020", 80)
Student3 = school("Ayush Rai", "01211402020", 65)

print(Student1)
print()
print(Student2)
print()
print(Student3)
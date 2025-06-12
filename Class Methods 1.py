# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

# instance method
    def get_info(self):
        return f"{self.name} : {self.gpa}"

# class method
    @classmethod
    def get_count(cls):
        return f"Total number of student is: {cls.count}"

student1 = Student("Emmanuel", 4.25)
student2 = Student("Oiza", 4.15)
student3 = Student("Chuks", 4.00)
student4 = Student("Praise", 4.10)

print(Student.get_count())


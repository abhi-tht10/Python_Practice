

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
    
    def set_name(self, age):
        self.age = age

    def set_name(self, grade):
        self.grade = grade

class School:
    
    def __init__(self, name):
        self.name = name
        self.students = []
        self.staff = []

    def add_student(self, student):
        self.students.append(student)
    



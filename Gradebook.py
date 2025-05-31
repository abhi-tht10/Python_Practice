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
    
    def add_staff(self, staff):
        self.staff.append(staff)
    
    def get_students(self):
        return self.students
    
    def get_staff(self):
        return self.staff

s1 = Student("Kyle",20,99.2)
s2 = Student("Julie", 21, 93.5)

college1 = School("Columbia")
college1.add_student(s1)
college1.add_student(s2)
print(college1.get_students())



x = 10
y = 5

print(x+y)

l = 15
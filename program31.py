class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade


student1 = Student("John", 18, 12)
student1.display_student() 

setattr(student1, 'age', 19) 
print(getattr(student1, 'age')) 

student1.set_grade(11) 
print(student1.get_grade()) 

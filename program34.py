class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display_student(self):
        print(f"Roll No: {self.rollno}, Name: {self.name}, Gender: {self.gender}, Age: {self.age}")

class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display_course(self):
        super().display_student()
        print(f"Course Name: {self.coursename}, Duration: {self.duration}, Fee: {self.fee}")


c = Course(123, "John", "Male", 20, "Python Programming", "3 months", 5000)
c.display_course() 

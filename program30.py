class Student:
    def __init__(self):
        self.student_list = []

    def add_student(self, name, age, grade):
        student = {"name": name, "age": age, "grade": grade}
        self.student_list.append(student)

    def display_students(self):
        for student in self.student_list:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    def delete_student(self, name):
        for student in self.student_list:
            if student['name'] == name:
                self.student_list.remove(student)

    def search_student(self, name):
        for student in self.student_list:
            if student['name'] == name:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                return
        print(f"{name} is not found")


students = Student()
students.add_student("John", 18, 12)
students.add_student("Jane", 17, 11)
students.add_student("Alice", 16, 10)

students.display_students() 
students.delete_student("Jane")
students.search_student("Alice")

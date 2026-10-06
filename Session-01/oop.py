class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def show_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Major:", self.major)
        print("--------------------")

student1 = Student("Ali", 1001, "Computer Science")
student2 = Student("Sara", 1002, "Electrical Engineering")

student1.show_info()
student2.show_info()


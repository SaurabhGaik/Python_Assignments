class Student:
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @staticmethod
    def is_adult(age):
        return age >= 18

    def display_info(self):
        print("Name:", self.name, "Age:", self.age)


student1 = Student("Alice", 20)
student2 = Student("Bob", 17)

student1.display_info()
student2.display_info()

print("Total students:", Student.get_student_count())

print("Is Bob an adult?", Student.is_adult(student2.age))

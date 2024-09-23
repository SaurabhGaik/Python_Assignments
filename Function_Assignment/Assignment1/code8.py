class Student:
    school_name = "ABC School" 

    def __init__(self, name, grade): 
        self.name = name  
        self.grade = grade 
    def display_info(self):  
        return f"{self.name} studies in grade {self.grade} at {Student.school_name}."

name = input("Enter student name: ")
grade = input("Enter student grade: ")

# Creating an instance with user input
student1 = Student(name, grade)
print(student1.display_info())  

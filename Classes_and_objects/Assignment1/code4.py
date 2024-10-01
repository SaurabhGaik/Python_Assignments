class Parent:
    def __init__(self):
        self.value = "This is Parent class"
    def show(self):
        print(self.value)
        
class Child(Parent):
    def __init__(self):
        self.value = "This is Child class"
    
    def show(self):
        print(self.value)

obj = Child()
obj.show()


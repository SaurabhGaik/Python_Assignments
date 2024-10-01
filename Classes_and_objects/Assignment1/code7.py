class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} is created")

    def __del__(self):
        print(f"Object {self.name} is destroyed")

obj1 = MyClass("obj1")
obj2 = MyClass("obj2")
obj3 = MyClass("obj3")
obj4 = MyClass("obj4")

obj3 = obj1

del obj2

print("End of program")



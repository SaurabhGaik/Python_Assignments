class Parent:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print("In  instance method")
    
    @classmethod
    def class_method(cls):
        print("In class method")

    @staticmethod
    def static_method():
        print("In static method")

class Child(Parent):
    pass

child_obj = Child("Child Instance")

child_obj.instance_method()    
child_obj.class_method()       
child_obj.static_method()      

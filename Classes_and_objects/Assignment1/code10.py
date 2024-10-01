class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("lets go")

my_car = Car()
my_car.start_engine()
my_car.drive()

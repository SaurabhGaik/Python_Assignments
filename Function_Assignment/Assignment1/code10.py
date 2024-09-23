
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Car: {self.year} {self.make} {self.model}"
    
def create_car_instance(make, model, year):
    return Car(make, model, year)

car_instance = create_car_instance("Toyota", "Camry", 2022)
print(car_instance.display_info())

# Parent Vehicle class
class Vehicle:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        

    def accelerate(self):
        self.speed += 10
        print(self.model, "accelerates to", self.speed, "km/h.")

    def brake(self):
        self.speed -= 10
        print(self.model, "slows down to", self.speed, "km/h.")

    def honk(self):
        print(self.model, "honks: Boom boom!")


class SportsCar(Vehicle):
    def accelerate(self):
        self.speed += 20 
        print(self.model, "sports car accelerates quickly to", self.speed, "km/h.")

    def honk(self):
        print(self.model, "sports car honks: Vroom Vroom!")


vehicle_obj = Vehicle("Toyota", "Corolla", 2022)
vehicle_obj.accelerate()
vehicle_obj.brake()
vehicle_obj.honk()

sports_car_obj = SportsCar("Ferrari", "F8", 2023)
sports_car_obj.accelerate()
sports_car_obj.brake()
sports_car_obj.honk()






class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.type = car_type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, car_type):
        self.type = car_type

    def set_color(self, color):
        self.color = color

car = Car("Красный", "Седан", 2020)
car.start()
car.stop()
car.set_year(2021)
car.set_type("Хэтчбек")
car.set_color("Синий")

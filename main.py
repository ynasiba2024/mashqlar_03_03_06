class Car:
    def __init__(self, model, speed):
        self.model = model
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

c = Car("BMW", 120)
print(c.speed)
c.speed = 180
print(c.speed)

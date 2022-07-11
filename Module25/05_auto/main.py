from math import sin, cos

class Transport:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, direction, distance):
        self.x = self.x + distance * cos(direction)
        self.y = self.y + distance * sin(direction)

    def __str__(self):
        return f'X : {self.x}, Y : {self.y}'



class Car(Transport):

    def __init__(self, x, y, direction):
        super(Car, self).__init__(x, y, direction)

class Bus(Transport):
    money = 0
    list_passengers = list()

    def __init__(self, x, y, direction, *args):
        super(Bus, self).__init__(x, y, direction)
        for passenger in args:
            if len(self.list_passengers) < 50:
                self.list_passengers.append(passenger)
            else:
                raise ValueError('Превышен лимит пассажиров')

    def get(self, name):
        if len(self.list_passengers) < 50:
            self.list_passengers.append(name)
        else:
            raise ValueError('Превышен лимит пассажиров')

    def go_out(self, name):
        try:
            self.list_passengers.remove(name)
        except ValueError:
            print('Такого пассажира нету')

    def move(self, direction, distance):
        self.x = self.x + (distance * cos(direction))
        self.y = self.y + (distance * sin(direction))
        self.money += distance // 5 * len(self.list_passengers)

    def __str__(self):
        return super().__str__() + f"\nЗаработанные деньги: {self.money}, Пассажиры: {', '.join(self.list_passengers)}"


bus = Bus(0, 0, 0, 'Вася', 'Петя')
car = Car(0, 0, 0)
print(bus)
bus.move(90, 1000)
print(bus)
bus.get('Анатолий')
bus.move(90, 1000)
print(bus)

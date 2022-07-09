class Person:

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def __str__(self):
        return f'Привет меня зовут {self.__first_name} {self.__last_name} Мне {self.__age} лет'

class Employee(Person):
    def salary(self):
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата {int(round(self.salary(), 0))}'

class Manager(Employee):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def salary(self):
        return 13000

class Agent(Employee):

    def __init__(self, first_name, last_name, age, sales):
        super().__init__(first_name, last_name, age)
        self.sales = sales

    def salary(self):
        return 5000 + .05 * int(self.sales)

class Worker(Employee):

    def __init__(self, first_name, last_name, age, hours):
        super().__init__(first_name, last_name, age)
        self.hours = hours
    def salary(self):
        return 100 * self.hours


manager1 = Manager('Вася', 'Первый', 23)
manager2 = Manager('Вася', 'Второй', 27)
manager3 = Manager('Вася', 'Третий', 40)
agent1 = Agent('Иван', 'Первый', 30, 20000)
agent2 = Agent('Иван', 'Второй', 30, 40000)
agent3 = Agent('Антон', 'Третий', 30, 60000)
worker1 = Worker('Антон', 'Первый', 30, 10)
worker2 = Worker('Антон', 'Второй', 30, 20)
worker3 = Worker('Антон', 'Третий', 30, 30)

print(manager1)
print(manager2)
print(manager3)
print(agent1)
print(agent2)
print(agent3)
print(worker1)
print(worker2)
print(worker3)


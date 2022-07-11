from termcolor import cprint
from random import randint

fur_coat = 0
full_money = 0
full_food = 0

class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.food_cat = 30
        self.clin = 0

    def __str__(self):
        return 'еды осталось {} для кота {}, денег осталось {}, чисота {}'.format(self.food, self.food_cat, self.money, self.clin)

class people:

    def __init__(self, name):
        self.fullness = 30
        self.name = name
        self.house = home
        self.joy = 100

    def eat(self):
        global full_food
        if self.house.food >= 30:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
            full_food += 30
        else:
            cprint('в доме нет еды', color='red')

    def pit_cat(self):
        self.joy += 5
        cprint('{} погладил кошку'.format(self.name), color='magenta')

    def __str__(self):
        return 'я - {}, сытость {}, счастье {}'.format(self.name, self.fullness, self.joy)

class Husband(people):


    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        if self.joy <= 10:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            return
        if self.house.clin >= 90:
            self.joy -= 10
        if self.fullness < 100 and self.house.food >= 30:
            self.eat()
        elif self.house.money <= 300:
            self.work()
        else:
            if self.joy <= 100:
                if 7 < randint(1, 11):
                    self.gaming()
                else:
                    self.pit_cat()
            else:
                self.work()


    def work(self):
        global full_money
        self.fullness -= 10
        self.house.money += 150
        full_money += 150
        cprint('{} сходил на работу'.format(self.name), color='red')

    def gaming(self):
        self.fullness -= 10
        self.joy += 20
        cprint('{} играл весь день'.format(self.name), color='red')

class Wife(people):

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла от голода'.format(self.name), color='red')
            return
        if self.joy <= 10:
            cprint('{} умерла от депрессии'.format(self.name), color='red')
            return
        if self.house.food <= 150 and self.house.money >= 150:
            self.shopping()
        elif self.fullness < 30 and self.house.food >= 30:
            self.eat()
        elif self.house.clin >= 30:
            self.clean_house()
        elif self.house.food_cat < 30:
            self.buy_food_cat()
        else:
            if self.house.money > 350:
                self.buy_fur_coat()
            else:
                self.pit_cat()


    def shopping(self):
        if self.house.money >= 150:
            cprint('{} сходила в магазин'.format(self.name), color='green')
            self.house.money -= 150
            self.house.food += 150
        else:
            cprint('дома нету денег', color='red')

    def buy_food_cat(self):
        self.house.money -= 50
        self.house.food_cat += 50

    def buy_fur_coat(self):
        global fur_coat
        if self.house.money >= 350:
            cprint('{} купила шубу'.format(self.name), color='cyan')
            self.house.money -= 350
            self.joy += 60
            fur_coat += 1
        else:
            cprint('нет денег', color='red')

    def clean_house(self):
        if self.house.clin <= 100:
            cprint('{} делает уборку'.format(self.name), color='green')
            self.house.clin = 0


class Cat:

    def __init__(self, name):
        self.fullness = 30
        self.name = name
        self.house = home

    def __str__(self):
        return 'я - {}, сытость {}'.format(self.name, self.fullness)

    def act(self):
        self.fullness -= 10
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        if self.fullness <= 30:
            self.eat()
        else:
            if 5 > randint(1, 11):
                self.sleep()
            else:
                self.soil()

    def eat(self):
        if self.house.food_cat > 10:
            self.house.food_cat -= 10
            self.fullness += 20
        else:
            cprint('В доме нет еды', color='red')


    def sleep(self):
        cprint('{} весь день спал'.format(self.name), color='magenta')

    def soil(self):
        self.house.clin += 5
        cprint('{} подрал обои'.format(self.name), color='magenta')

class Child:

    def __init__(self, name):
        self.fullness = 20
        self.name = name
        self.house = home
        self.joy = 100

    def __str__(self):
        return 'я - {}, сытость {}, счастье {}'.format(self.name, self.fullness, self.joy)

    def act(self):
        self.fullness -= 10
        if self.fullness <= 0:
            cprint('{} умерла от голода'.format(self.name), color='red')
            return
        if self.fullness <= 20:
            self.eat()
        else:
            self.sleep()


    def eat(self):
        self.fullness += 10
        self.house.food -= 10
        cprint('{} поел'.format(self.name), color='blue')

    def sleep(self):
        cprint('{} весь день спал'.format(self.name), color='blue')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(home, color='cyan')
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
print('всего шуб куплено {}, всего денег заработано {}, всего еды съедено {}'.format(fur_coat, full_money, full_food))
# TODO после реализации первой части - отдать на проверку учителю

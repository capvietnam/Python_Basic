class Property:
    worth = 0

    def __init__(self, worth):
        self.worth = worth

class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


money = float(input('Введите количество имеющихся денег: '))
print('Введите стоимость имущества: ')

wroth_1 = float(input('Квартира: '))
nalog_appart = Apartment(wroth_1)
print(f'Налог на квартиру {nalog_appart.tax()}')

wroth_2 = float(input('Машина: '))
nalog_car = Car(wroth_2)
print(f'Налог на машину {nalog_car.tax()}')

wroth_3 = float(input('Дача: '))
nalog_contrhous = CountryHouse(wroth_3)
print(f'Налог на дачу {nalog_contrhous.tax()}')

sum_nalog = nalog_appart.tax() + nalog_car.tax() + nalog_contrhous.tax()


if sum_nalog >= money:
    print(f'Всего налога на сумму {sum_nalog}, а у вас только {money}')
    print('Денег не хватает')
else:
    print(f'Всего налога на сумму {format(sum_nalog)}\nОтлично, денег хватает ')
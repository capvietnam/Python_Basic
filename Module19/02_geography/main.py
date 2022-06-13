quantity = int(input('Количество стран: '))
dict_country = dict()
n = 0

for number in range(quantity):
    all1 = [i for i in input(f'{number + 1} страна: ').split()]
    for city in all1[1:]:
        dict_country[city] = all1[0]

while True:
    n += 1
    country = input(f'\n{n} город: ')
    if dict_country.get(country):
        print(f'Город {country} расположен в стране {dict_country.get(country)}.')
    else:
        print(f'По городу {country} данных нет.')
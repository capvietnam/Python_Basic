guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

new_guests = None

while new_guests != 'Пора спать':
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    action = input('Гость пришёл или ушёл? ').lower()

    if action == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break

    new_guests = input('Имя гостя: ')
    if action == 'пришёл':
        if len(guests) < 6:
            print(f'Привет, {new_guests}')
            guests.append(new_guests)
        else:
            print(f'Прости, {new_guests}, но мест нет.')
    elif action == 'ушёл':
        print(f'Пока, {new_guests}')
        guests.remove(new_guests)
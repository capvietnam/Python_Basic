while True:
    quantity_numbers = 0
    quantity_uppers = 0
    password = input('Придумайте пароль: ')
    for i in password:
        if i.isnumeric():
            quantity_numbers += 1
        if i == i.upper():
            quantity_uppers += 1
    if quantity_numbers > 2 and quantity_uppers > 0 and len(password) > 7:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')



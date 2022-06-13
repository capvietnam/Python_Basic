goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key_good in goods.keys():
    prise_all = 0
    quntity_good = 0
    good = goods.get(key_good)
    for list_in_stor in store[good]:
        prise_all += list_in_stor['quantity'] * list_in_stor['price']
        quntity_good += list_in_stor['quantity']
    print(f'{key_good} — {quntity_good} штук, стоимость {prise_all} рубля')

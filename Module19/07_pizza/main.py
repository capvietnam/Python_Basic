quantity = int(input('Введите количество заказов: '))
orders_data = dict()

for i in range(1, quantity + 1):
    name, pizza, amount = input(f'{i} заказ: ').split()
    amount = int(amount)
    if name not in orders_data:
        orders_data[name] = {pizza: amount}
    else:
        if pizza not in orders_data[name]:
            orders_data[name][pizza] = amount
        else:
            orders_data[name][pizza] += amount

for fio, order in sorted(orders_data.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('\t', pizza, amount)
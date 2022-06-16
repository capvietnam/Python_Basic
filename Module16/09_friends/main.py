quantity_friends = int(input('Кол-во друзей: '))
quantity_debit = int(input('Долговых расписок: '))
list_friends = []

for i in range(1, quantity_friends + 1):
    list_friends.append([i, 0])

for t in range(quantity_debit):
    print(f'{t+1}-я расписка')
    who_should = int(input('Кому: '))
    who_gave = int(input('От кого: '))
    how_many = int(input('Сколько: '))
    list_friends[who_should-1][1] -= how_many
    list_friends[who_gave-1][1] += how_many

print('Баланс друзей:')
for i in list_friends:
    print(f'{i[0]} : {i[1]}')
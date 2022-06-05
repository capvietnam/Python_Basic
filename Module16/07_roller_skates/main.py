quanitu = 0
max_quanitu = 0
peoples = []
skates = []

quanitu_skates = int(input('Кол-во коньков: '))
for i in range(quanitu_skates):
    skates.append(input(f'Размер {i+1}-й пары: '))

quanitu_peoples = int(input('\nКол-во людей: '))
for t in range(quanitu_peoples):
    peoples.append(input(f'Размер {t+1}-й человека: '))

for people in peoples:
    for skate in skates:
        if skate >= people:
            quanitu += 1
    if quanitu >  max_quanitu:
        max_quanitu = quanitu
    quanitu = 0

print('Наибольшее кол-во людей, которые могут взять ролики:', max_quanitu)
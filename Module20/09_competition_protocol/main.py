list_competitions = list()
quantity = int(input('Сколько записей вносится в протокол? '))
print('Записи(результат и имя): ')
rez, fio = input('1-я запись: ').split()
list_competitions.append([int(rez), fio])

for n in range(1, quantity):
    print(list_competitions)
    rez, fio = input(f'{n+1}-я запись: ').split()
    rez = int(rez)
    for i in list_competitions:
        if i[1] == fio and i[0] <= rez:
            list_competitions.remove(i)
            break
    for s in list_competitions:
        if s[1] == fio and s[0] >= rez:
            break
    else:
        for t in list_competitions:
            if t[0] >= rez:
                list_competitions.insert(list_competitions.index(t), [rez, fio])
                break
        else:
            list_competitions.append([rez, fio])

print('1-е место.', list_competitions[-1][1], list_competitions[-1][0],
'\n2-е место.', list_competitions[-2][1], list_competitions[-2][0],
'\n3-е место.', list_competitions[-3][1], list_competitions[-3][0])
print(list_competitions)


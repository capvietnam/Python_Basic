dict_base = {}

def search(scan):
    for key, value in dict_base.items():
        if scan in key or scan + 'а' in key or scan[:-1] in key:
            print(key[0], key[1], value)

def new_number(fio, number):
    if fio in dict_base.keys() and number in dict_base.values():
        print('Такой человек уже есть в контактах.')
    else:
        dict_base[fio] = number
        print('Текущий словарь контактов:', dict_base)


while True:
    action = input('1. Добавить контакт\n2. Найти человека\nВведите номер действия: ')
    if action == '1':
        new_number(fio=tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split()),
                   number=int(input('Введите номер телефона: ')))
    elif action == '2':
        search(scan=input('Введите фамилию: ').title())
    else:
        print('Неверное действие')

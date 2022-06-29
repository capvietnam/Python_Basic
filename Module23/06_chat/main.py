with open('messenger.txt', '2', encoding='utf-8') as file:
    pass

while True:
    name = input('Введите имя: ')
    action = input('1 - Посмотреть текущий текст чата.\n2 - Отправить сообщение\n1 или 2: ')
    if action == '2':
        with open('messenger.txt', 'a', encoding='utf-8') as file:
            file.write(name + ': ' + input('Ввведите текст')+ '\n')
    elif action == '1':
        try:
            with open('messenger.txt', 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print('пока нету истории')

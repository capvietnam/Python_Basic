import os


new_str = input('Введите строку: ')
print(os.path.abspath('main.py'))
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
way = ''
for i in input().split():
    way = os.path.join(way, i)
name_file = input('Введите имя файла: ')

if os.path.exists(os.path.abspath(os.path.join(os.path.sep, way, name_file))):
    if 'да' == input('Вы действительно хотите перезаписать файл? ').lower():
        file = open(os.path.abspath(os.path.join(os.path.sep, way, name_file)), 'w')
        file.write(new_str)
        file.close()
else:
    file = open(os.path.abspath(os.path.join(os.path.sep, way, name_file)), 'w', encoding='utf-8')
    file.write(new_str)
    file.close()


# Users zenak Desktop projects pythonProject Python_Basic Module22 05_save
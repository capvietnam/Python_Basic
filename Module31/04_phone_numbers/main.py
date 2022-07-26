from re import findall


tel_list = ['9999999999', '999999-999', '99999x9999']

tel_patern_1 = r'[8, 9]\d{9}'

for number in tel_list:
    if findall(tel_patern_1, number):
        text = 'всё в порядке'
    else:
        text = 'не подходит'
    print(f'{tel_list.index(number) + 1}й номер:', text)

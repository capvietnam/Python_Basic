# TODO здесь писать код
while True:
    list_number_ip = input('Введите IP: ').split('.')
    if len(list_number_ip) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
    else:
        break

for number in list_number_ip:
    if number.isnumeric() == False:
        print(f'{number} — это не целое число.')
        break
    elif int(number) >  255:
        print(f'{number} превышает 255.')
        break
    elif 0 > int(number):
        print(f'{number} меньше 0.')
        break
else:
    print('IP-адрес корректен.')

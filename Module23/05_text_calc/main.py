total_summ = 0


def transformation(str_text):
    str_list_text = str_text.split()
    number1 = int(str_list_text[0])
    number2 = int(str_list_text[2])
    action = str_list_text[1]
    calculation(number1, action, number2)

def calculation(number1, action, number2):
    global total_summ, str_text
    try:
        if action == '+':
            total_summ += number1 + number2
        elif action == '*':
            total_summ += number1 * number2
        elif action == '/':
            total_summ += number1 / number2
        elif action == '**':
            total_summ += pow(number1, number2)
        else:
            raise SyntaxError
    except Exception:
        print(f'Обнаружена ошибка в строке: {str_text}', end='')
        if input('Хотите исправить? ').lower() == 'да':
            str_text = input('Введите исправленную строку: ')
            transformation(str_text)
    print(total_summ)


with open('calc.txt', 'r', encoding='utf-8') as file:
    for str_text in file:
        transformation(str_text)





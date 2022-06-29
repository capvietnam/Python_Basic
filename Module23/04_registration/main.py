reg = open('registrations.txt', 'r', encoding='utf-8')
good = open('registrations_good.log', 'w', encoding='utf-8')
bad = open('registrations_bad.log', 'w', encoding='utf-8')

def F(str_list_file):
    try:
        if len(str_list_file) != 3:
            raise IndexError
        elif str_list_file[0].isalpha() == False:
            raise NameError
        elif str_list_file[2].isdigit():
            if 10 > int(str_list_file[2]) or 99 < int(str_list_file[2]):
                raise ValueError
        elif '.' not in str_list_file[1] or '@' not in str_list_file[1]:
            raise SyntaxError
    except IndexError:
        bad.write(str_file[:-1] + '\t\tНЕ присутствуют все три поля:\n')
    except NameError:
        bad.write(str_file[:-1] + '\t\tПоле «Имя» содержит НЕ только буквы:\n')
    except ValueError:
        bad.write(str_file[:-1] + '\t\tПоле «Возраст» НЕ является числом от 10 до 99:\n')
    except SyntaxError:
        bad.write(str_file[:-1] + '\t\tПоле «Имейл» НЕ содержит @ и . (точку):\n')
    else:
        good.write(str_file)

try:
    for str_file in reg.readlines():
        str_list_file = str_file.split()
        F(str_list_file)
except Exception:
    print('Что то пошло не так!')
finally:
    reg.close()
    good.close()
    bad.close()



dict_base = {('Сидоров', 'Никита'): 35, ('Сидорова', 'Алина'): 34, ('Сидоров', 'Павел'): 10}

scan = input('Введите фамилию: ').title()

for key, value in dict_base.items():
    if scan or scan+'а' or scan[:-2] in key:
        print(key[0], key[1], value)
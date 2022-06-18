students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

set_interests = set()
len_all_surname = 0
list_id_old = list((id_student, value['age']) for id_student, value in students.items())

for key in students.keys():
    len_all_surname += len(students[key]['surname'])
    set_interests.update(students[key]['interests'])

print('Список пар "ID студента — возраст":', list_id_old)
print('Полный список интересов всех студентов:', set_interests)
print('Общая длина всех фамилий студентов:', len_all_surname)

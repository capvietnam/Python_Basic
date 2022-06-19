import re


stroka = input('Строка: ')
corteg = tuple(int(i) for i in re.findall(r'-?\d+\.?\d*', input('Кортеж чисел: ')))
zip_new = ((stroka[i], corteg[i]) for i in range(len(stroka)))
print(zip_new)
for t in zip_new:
    print(t)
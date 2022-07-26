from requests import get
from json import loads, dump, load


my_req = get('https://www.breakingbadapi.com/api/deaths')
data = loads(my_req.text)
max_death = 0
for elem in data:
    if elem['number_of_deaths'] > max_death:
        max_death = elem['number_of_deaths']
for elem in data:
    if elem['number_of_deaths'] == max_death:
        with open('max_death.json', 'w') as file:
            dump(elem, file)
with open('max_death.json', 'r') as file:
    data = load(file)
    for elem in data:
        print(elem + ':', data[elem])
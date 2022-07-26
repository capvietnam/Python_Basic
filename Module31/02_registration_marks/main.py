from re import findall

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

taxi_patern = r'\b\w{2}\d{3}\d{2,3}\b'
private_cars_patern = r'\b\w{1}\d{3}\w{2}\d{2,3}\b'

search_taxi = findall(taxi_patern, text)
private_cars_search = findall(private_cars_patern, text)

print('Список номеров частных автомобилей:', private_cars_search)
print('Список номеров такси:', search_taxi)

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
oll_time = 0
for i in range(int(input('Сколько песен выбрать? '))):
    while True:
        name = input(f'Название {i+1} песни: ')
        if name in violator_songs.keys():
            oll_time += violator_songs.setdefault(name)
            break
print('\nОбщее время звучания песен:', round(oll_time, 2), 'минуты')


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

quantity = int(input('Сколько песен выбрать? '))
summ_time = 0
for i in range(quantity):
    song = input(f'Название {i + 1} песни: ')
    for i in violator_songs:
        if i[0] == song:
            summ_time += i[1]

print(f'Общее время звучания песен: {round(summ_time, 2)} минуты')
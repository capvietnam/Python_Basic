site = {
    'html': {
        'head': {
            'title': 'Мой сайт'},
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

# def seach(seach_key, depth):
#     if depth == 'y':
#         max_depth = int(input('Введите максимальную глубину: '))
#     else:
#         max_depth = None
#     for key in site.keys():
#         if key == seach_key:
#             return site[key]
#         elif max_depth == 1:
#             return None
#         for key1 in site[key]:
#             if key1 == seach_key:
#                 return site[key][key1]
#             elif max_depth == 2:
#                 return None
#             for key2 in site[key]:
#                 if key2 == seach_key:
#                     return site[key][key1][key2]
#                 else:
#                     return None
#
#
# print('Значение ключа:', seach(seach_key=input('Введите искомый ключ: '),
#       depth=input('Хотите ввести максимальную глубину? Y/N: ').lower())
# )
def seach(seach_key, max_depth=0, sites=site):
    max_depth -= 1
    for key in sites.keys():
        if key == seach_key:
            return sites[key]
        elif max_depth == 0:
            return None
        elif type(sites[key]) == dict:
            return seach(seach_key=seach_key, max_depth=max_depth, sites=sites[key])

seach_key = input('Введите искомый ключ: ')
depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if depth == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
else:
    max_depth = 0

print('Значение ключа:', seach(seach_key=seach_key, max_depth=max_depth))
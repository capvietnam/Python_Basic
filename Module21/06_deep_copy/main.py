site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
quantity = int(input('Сколько сайтов: '))
def new_site(new_prod):
    global quantity
    quantity -= 1
    site['html']['head']['title'] = f'Куплю/продам {new_prod} недорого'
    site['html']['body']['h2'] = f'У нас самая низкая цена на {new_prod}'
    print(f'Сайт для {new_prod}:\n', 'site =', site)
    if quantity == 0:
        return
    new_site(new_prod=input('Введите название продукта для нового сайта: '))


new_site(new_prod=input('Введите название продукта для нового сайта: '))
from pprint import pformat
from yapf.yapflib.yapf_api import FormatCode
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

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + '\t\t' + "'"+str(key)+"':")
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + '\t\t' + "'"+str(value)+"'")

def new_site(new_prod):
    global quantity
    quantity -= 1
    site['html']['head']['title'] = f'Куплю/продам {new_prod} недорого'
    site['html']['body']['h2'] = f'У нас самая низкая цена на {new_prod}'
    formatted_code, _ = FormatCode(pformat(site))
    print(f'Сайт для {new_prod}:\n', "site =", formatted_code)
    if quantity == 0:
        return
    new_site(new_prod=input('Введите название продукта для нового сайта: '))


new_site(new_prod=input('Введите название продукта для нового сайта: '))
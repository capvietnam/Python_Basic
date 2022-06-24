## Задача 6. Глубокое копирование
### Что нужно сделать
Вы сделали для заказчика структуру сайта по продаже телефонов:
```python
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': 'Продать'
		}
	}
}
```

Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт, только для своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за работу. 

Напишите программу, которая запрашивает у клиента, сколько будет сайтов, а затем запрашивает название продукта и после каждого запроса выводит на экран активные сайты. 

Условия: структуру сайта нужно описать один раз, копипасту никто не любит.

Подсказка: используйте рекурсию.

Пример:
```
Сколько сайтов: 2
Введите название продукта для нового сайта: iPhone
Сайт для iPhone: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам iPhone недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}

Введите название продукта для нового сайта: Samsung
Сайт для iPhone: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам iPhone недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}

Сайт для Samsung: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам Samsung недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на Samsung',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}
```

### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- input содержит корректные приглашения для ввода. 
- Основной функционал описан в отдельной функции(-ях).
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

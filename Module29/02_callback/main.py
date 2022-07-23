from collections.abc import Callable
import functools


app = {}


def callback(route: str) -> Callable:

    def wrapped(func: Callable) -> Callable:
        app[route] = func
        @functools.wraps(func)
        def wrapper():
            ret = func()
            return ret

        return wrapper

    return wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')


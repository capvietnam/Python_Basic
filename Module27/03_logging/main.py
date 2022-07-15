import logging
import time
from datetime import datetime
from typing import Any, Callable


def loging(func) -> Callable:
    """"декоратор, логирующий работу кода в файл function_errors.log"""
    def wrapped_func(*args, **kwargs) -> Any:
        with open('function_errors.log', 'w') as file:
            try:
                print(f'Вызывается функция - {wrapped_func.__name__}\n'
                      f'Позиционные аргументы {args}\n'
                      f'Именованные аргументы {kwargs}')
                result = func(*args, **kwargs)
                return result
            except Exception as exept:
                print(f'функция - ({func.__name__}) ошибка - {exept},'
                      f' время : {datetime.today()}', file=file)
    return wrapped_func

@loging
def test(age: int):
    print('<Тут что-то происходит...>')
    print(str(age))
    print(print(jhjh))





test1 = test(51)
print(test1)
from typing import Any, Callable


def loging(func) -> Callable:
    """"декоратор, выводящий имя и значения функции"""
    name_func = func.__name__
    def wrapped_func(*args, **kwargs) -> Any:
        print("Вызывается {}({})".format(
            func.__name__,
            ", ".join(list(str(arg) for arg in args)+
                list('='.join((str(k), str(v))) for k, v in kwargs.items())
                      )
        ))
        result = func(*args, **kwargs)
        print(f'{name_func} вернула значение {result}')
        print(result)
        return result
    return wrapped_func

@loging
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
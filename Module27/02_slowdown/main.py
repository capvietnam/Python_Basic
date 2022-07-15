import time
from typing import Any, Callable


def how_are_you(func) -> Callable:
    """"надоедливый декоратор"""
    def wrapped_func(*args, **kwargs) -> Any:
        time.sleep(4)
        result = func(*args, **kwargs)
        return result
    return wrapped_func

@how_are_you
def test():
    print('<Тут что-то происходит...>')




test1 = test()
print(test1)
from typing import Callable
import functools


def singleton(cls):
    functools.wraps(cls)
    def wraper_singleton(*args, **kwargs):
        if not wraper_singleton.instance:
            wraper_singleton.instance = cls(*args, **kwargs)
        return wraper_singleton.instance
    wraper_singleton.instance = None
    return wraper_singleton

@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
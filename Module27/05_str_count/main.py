def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    func.__invocation_count__ = 0
    def wrapper(*args, **kwargs):
        func.__invocation_count__ += 1
        res = func(*args, **kwargs)
        print(f"{func.__name__} была вызвана: {func.__invocation_count__} раза")
        return res

    return wrapper

@counter
def func1():
    pass

func1()
func1()
func1()
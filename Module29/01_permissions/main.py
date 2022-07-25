from collections.abc import Callable
import functools


user_permissions = ['admin']


def check_permission(permissions: str) -> Callable:
    def check_permission1(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if permissions == 'admin':
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapper

    return check_permission1


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

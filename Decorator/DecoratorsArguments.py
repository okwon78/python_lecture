"""
Decorator with Arguments
"""


def prefix_decorator(prefix):
    def decorator_func(orgi_func):
        def wrapper_func(*args, **kwargs):
            print(prefix, "wrapper_func")
            return orgi_func(*args, **kwargs)

        return wrapper_func

    return decorator_func


class decorator_class_1(object):
    def __init__(self, prefix):
        print(f'__init__ {prefix}')

    def __call__(self, func):
        print(f'__call__ {func}')
        return func


class decorator_class_2(object):
    def __init__(self):
        print(f'__init__')

    def __call__(self, param=[]):
        print(f'__call__ {param}')

        def decorator_func(orgi_func):
            print(f'wrapper_func {orgi_func}')

            # def wrapper_func(*args, **kwargs):
            #     return orgi_func(*args, **kwargs)

            return orgi_func

        return decorator_func


# @prefix_decorator("prefix")
# def hello_func():
#     print('hello_func', '\n')


# @decorator_class_1("prefix")
# def hello_class_1():
#     print('hello_class_1', '\n')

d = decorator_class_2()
b = decorator_class_2()

@b(param=['c', 'd'])
@d(param=['a', 'b'])
def hello_class_2():
    print('hello_class_2', '\n')


if __name__ is '__main__':
    # hello_func()
    hello_class_2()

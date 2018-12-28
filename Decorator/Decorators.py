from functools import wraps

"""
Decorator using Function

the following is a basic form of decorators using function.
functools.wraps gets ride of cascaded wrapper_functions.
"""


def decorator_func_1(original_func):
    @wraps(original_func)
    def wrapper_func_1(*args, **kwargs):
        print(f"wrapper_func_1: {original_func.__name__}")
        return original_func(*args, **kwargs)

    return wrapper_func_1


def decorator_func_2(original_func):
    @wraps(original_func)
    def wrapper_func_2(*args, **kwargs):
        print(f"wrapper_func_2: {original_func.__name__}")
        return original_func(*args, **kwargs)

    return wrapper_func_2


"""
Decorator using Class

The following is the way of implementing decorator using class.
However, decorator class does not have functools.wrap which decorator function has
Thus, decorator function is more prefer way to implement decorators.
"""


class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f"decorator_class_1 class {self.original_func.__name__}")
        return self.original_func(*args, **kwargs)


# @decorator_func_2
# @decorator_func_1
# def hello_world_1():
#     print('hello_world_1')


@decorator_class
@decorator_class
def hello_world_2():
    print('hello_world_2')


if __name__ is '__main__':
    # hello_world_1()
    print('\n')
    hello_world_2()

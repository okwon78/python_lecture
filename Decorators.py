# Decorators


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("wrapper func")
        original_func(*args, **kwargs)

    return wrapper_func


class decorator_class:
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("wrapper class")
        return self.original_func(*args, **kwargs)


@decorator_class
# @decorator_func
def display():
    print("Hi")


display()


@decorator_class
# @decorator_func
def display_arg(name, age):
    print(name, age)


display_arg("John", 24)


@decorator_func
@decorator_class
def stacked_decorator_func():
    print("stacked_decorator")


stacked_decorator_func()


# from functools import wraps



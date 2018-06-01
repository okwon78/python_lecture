
def prefix_decorator(prefix):
    def decorator_func(orgi_func):
        def wrapper_func(*args, **kwargs):
            print(prefix, "wrapper_func")
            return orgi_func(*args, **kwargs)

        return wrapper_func
    return decorator_func


@prefix_decorator("prefix")
def display():
    print('hi', '\n')

display()
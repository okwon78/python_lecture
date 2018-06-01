
def outer_func(message):

    def inner_func():
        print(message)

    # return inner_func()
    return inner_func


print(outer_func("Hi"))
print(outer_func("Hi").__name__)

# The most useful thing about closure is that it keep some value in the function, and then it reuse it
hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()








def square_numbers(nums):
    result = []

    for i in nums:
        result.append(i * i)

    return result


result = square_numbers(range(5))

print(result)


# Generator : It does not consume memory as much as list above. especially, It is very useful, when list is huge.
def square_numbers_generator(nums):
    for n in nums:
        # print('yield')
        yield n * n


print(list(square_numbers_generator(range(5))))

iterator = square_numbers_generator(range(5))

# print(next(Iter))
# print(next(Iter))
# print(next(Iter))

for i in iterator:
    print(i)


gen = (n * n for n in range(5))

for i in gen:
    print(i)

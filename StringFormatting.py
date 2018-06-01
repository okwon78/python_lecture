person = {'name': 'OB', 'age': 10}
my_list = [1, 2, 3, 4]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


comment = "{0[name]}, {0[age]}".format(person)
comment = "{0[0]}, {0[1]}".format(my_list)

p = Person('Kwon', 20)

comment = "{0.name} {0.age}".format(p)
comment = "{name} {age}".format(**person)


print(comment)

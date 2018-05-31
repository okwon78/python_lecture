class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scale = 2.0

    def size(self):
        return (self.width * self.height) * self.scale

    def name(self):
        print("Shape")


class Square(Shape):

    def __init__(self, width):
        super().__init__(width, width)

    def name(self):
        print("Square")


class Sphere(Shape):

    def __init__(self, width, height):
        super().__init__(width, height)

    def name(self):
        print("Sphere")


sh = Shape(1, 2)
sh.name()

sq = Square(1)
print(sq.size())
sq.name()

sp = Sphere(1, 1)
print(sp.size())
sp.name()


print(isinstance(sp, Sphere))
print(isinstance(sp, Shape))
print(isinstance(sp, Square))
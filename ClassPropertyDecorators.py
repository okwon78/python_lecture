class Rectangle:

    def __init__(self, width, height):
         self.width = width
         self.height = height

    @property
    def size(self):
        return self.width * self.height

    @size.setter
    def size(self, s):
        self.height = s / self.width

    @size.deleter
    def size(self):
        print("Delete Size")
        self.width = None
        self.height = None


rec1 = Rectangle(2, 2)
print(rec1.size)
rec1.size = 20
print(rec1.size)

del rec1.size

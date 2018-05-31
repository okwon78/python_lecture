class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        print("official string representation of an object.")

    def __str__(self):
        print("informal string representation of an object.")

    def size(self):
        return self.width * self.height

    def __add__(self, other):
        return self.size() + other.size()

    def __sub__(self, other):
        return NotImplemented

    def __len__(self):
        return self.width


print(1+2)
print(int.__add__(1, 2))
print(Shape(1, 1) + Shape(2, 2))
print(Shape(1, 1) - Shape(2, 2))

print(len("Hello world"))
print("Hello world".__len__())


print(len(Shape(2, 1)))
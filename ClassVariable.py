class Widget:
    # static variable
    count = 0

    def __init__(self, name):
        # access static variable
        Widget.count += 1
        self.name = name

w1 = Widget("A")
w2 = Widget("B")
w3 = Widget("C")

print(f"The number of instance: {w1.count}")
print(f"The number of instance: {w2.count}")
print(f"The number of instance: {w3.count}")

print("--------")
print(Widget.__dict__)
print("--------")
print(w1.__dict__)
print("--------")
w1.count = 10
print(f"w1: {w1.__dict__}")
print(f"w2: {w2.__dict__}")
print("--------")

print(f"The number of instance: {w1.count}")
print(f"The number of instance: {w2.count}")
print(f"The number of instance: {w3.count}")


def main():
    func("Hi")
    func("Hi", name="Jo")

    students("A", "B", "C", "D")
    students(a="A", b="B", c="C", d="D")
    students(1, 2, a="A", b="B")

    lectures = ["A", "B", "C"]
    student = {"name": "Kwon", "age": 20}

    students(lectures, student)
    students(*lectures, **student)


def func(greeting, name="Kwon"):
    print(f"{greeting}, {name}")


def students(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ is "__main__":
    main()

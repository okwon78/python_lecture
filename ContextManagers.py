# with open('sample.txt', 'w') as f:
#     f.write("AA")

# class
class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with OpenFile("sample.txt", 'w') as f:
    f.write("BBBBB")


# method
from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()


with open_file("sample.txt", 'w') as f:
    f.write('aaaaaa')

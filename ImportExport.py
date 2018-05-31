import my_first_module as mm
from my_second_module import greeting, thanks
import sys

def main():
    """ Imported my module"""

    lectures = ["A", "B", "C"]
    print(mm.find_index(lectures, "B"))
    print(mm.test)

    greeting()
    thanks()

    # PYTHONPATH
    print(sys.path)


if __name__ is "__main__":
    main()
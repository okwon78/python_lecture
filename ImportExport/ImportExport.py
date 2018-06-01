
import sys

from ImportExport import my_first_module
from ImportExport.my_second_module import greeting, thanks


def main():
    """ Imported my module"""

    lectures = ["A", "B", "C"]
    print(my_first_module.find_index(lectures, "B"))
    print(my_first_module.test)

    greeting()
    thanks()

    # PYTHONPATH
    print(sys.path)


if __name__ == "__main__":
    main()
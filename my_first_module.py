print("Imported my module")

test = "Test String"


def find_index(to_search, target):

    for index, value in enumerate(to_search):
        if value == target:
            return index

    return -1
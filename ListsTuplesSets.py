def main():
    empty_list = []
    empty_list = list()

    empty_tuple = ()
    empty_tuple = tuple()

    empty_set = {}
    empty_set = set()

    empty_dict = {}
    empty_dict = dict()

    # lists()
    # tuples()
    # sets()
    dictionaries()


def lists():
    lectures = ["Statistics", "Data structure", "Algorithms"]
    print(lectures)
    print(lectures[0])
    print(lectures[-1])

    lectures.append("Operating System")
    print(lectures)

    lectures.insert(2, "Database")
    print(lectures)

    new_lectures = ["C++", "Java"]
    lectures.extend(new_lectures)
    print(lectures)

    print(lectures[0:2])
    print(lectures[2:])
    print(lectures[:2])

    lectures.remove("Data structure")
    print(lectures)

    item = lectures.pop()
    print(item)
    item = lectures.pop()
    print(item)
    print(lectures)

    lectures.reverse()
    print(lectures)

    lectures.sort()
    print(lectures)

    lectures.sort(reverse=True)
    print(lectures)

    sorted_lectures = sorted(lectures)
    print(sorted_lectures)
    print(lectures)
    print(lectures.index("Database"))
    print("Database" in lectures)
    print("Art" in lectures)

    for lecture in lectures:
        print(lecture)

    for index, lecture in enumerate(lectures):
        print(index, lecture)

    lectures_str = ", ".join(lectures)
    print(lectures_str)

    new_lecture = lectures_str.split(", ")
    print(new_lecture)

    nums = [1, 4, 5, 3, 6, 8]
    print(min(nums))
    print(max(nums))
    print(sum(nums))


def tuples():
    # mutable
    list1 = ["A", "B", "C"]
    list2 = list1
    print(list1, list2)

    list1[0] = "D"
    print(list1, list2)

    # immutable
    tuple1 = ("A", "B", "C")
    tuple2 = tuple1
    print(tuple1, tuple2)

    # tuple1[0] = "D" <- tuple does not support item assignment


def sets():
    lectures = {"A", "B", "C"}
    print(lectures)

    lectures.add("A")
    print(lectures)

    another_lectures = {"B", "C", "D"}
    print(lectures.intersection(another_lectures))
    print(lectures.union(another_lectures))


def dictionaries():
    lectures = ["Statistics", "Data structure", "Algorithms"]
    student = {"lastName": "Kwon", "firstName": "Oh Beom", "lectures": lectures}
    print(student)
    print(student["lastName"])
    print(student["lectures"][0])

    # print(student["name"]) <- Emit KeyError
    print(student.get("name"))
    print(student.get("name", "Not Found"))

    student["phone"] = "010-1111-1234"
    print(student)

    student.update({"age": 30, "phone": "010-3333-4444"})
    print(student)

    del student["age"]
    print(student)

    print(student.pop("lectures"))
    print(student)

    print(len(student))

    print(student.keys())
    print(student.values())
    print(student.items())

    for key in student:
        print(key)

    for key, value in student.items():
        print(key, value)


if __name__ is "__main__":
    main()

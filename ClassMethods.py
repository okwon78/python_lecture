import datetime


class Student:
    name_of_school = ""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.name_of_school = "U of Florida"

    @classmethod
    def set_name_of_school(cls, name_of_school):
        cls.name_of_school = name_of_school
        print("class method")

    @classmethod
    def from_string(cls, string):
        name, grade = string.split("-")
        return cls(name, int(grade))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


s1 = Student("John", 1)
s2 = Student("Kwon", 2)

# Student.set_name_of_school("Stanford")
s1.set_name_of_school("UF")

print(Student.name_of_school)
print(s1.name_of_school)
print(s2.name_of_school)

s3 = Student.from_string("Romi-1")

today = datetime.datetime.now()
print(Student.is_workday(today))

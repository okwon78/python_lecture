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
        print(f'set name_of_school (class method) {name_of_school}')

    @classmethod
    def from_string(cls, string):
        name, grade = string.split("-")
        return cls(name, int(grade))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


john = Student("John", 1)
kwon = Student("Kwon", 2)

# Student.set_name_of_school("Stanford")
kwon.set_name_of_school("UF")

print(Student.name_of_school)
print('kwon: ', kwon.name_of_school)
print('john: ', john.name_of_school)

s3 = Student.from_string("Romi-1")

today = datetime.datetime.now()
print(Student.is_workday(today))

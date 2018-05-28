def main():

    nation = "Korea"

    if nation == "Korea":
        print("Nationality is Korean")

    nation = "US"
    if nation == "Korea":
        print("Nationality is Korea")
    elif nation == "US":
        print("Nationality is US")
    elif nation == "China":
        print("Nationality is China")
    else:
        print("Another country")

    # Python does not support switch case statement

    user = "admin"
    logged_in = False

    if user == "admin" and logged_in:
        print("go to admin page")
    else:
        print("go to default page")

    if not logged_in:
        print("Plz log in")
    else:
        print("Welcome")

    list1 = [1, 2, 3]
    list2 = [1, 2, 3]

    if list1 == list2:
        print("The both lists have the same values")
    else:
        print("those are different values")

    if list1 is list2:
        print("Those lists are the same instance")
    else:
        print("Those lists are different instances")

    print(id(list1), id(list2))

    list2 = list1
    if id(list1) == id(list2):
        print("Those lists are the same instance")
    else:
        print("Those lists are different instances")

    # False Values
    # 1. False
    # 2. None
    # 3. Zero of any numeric type
    # 4. Any empty data structure: list, tuple, set, dictionary

    empty_dict = {}

    if empty_dict:
        print("dictionary is not empty")
    else:
        print("dictionary is empty")


if __name__ in "__main__":
    main()

def main():

    nums = [1, 2, 3, 4]

    for num in nums:

        if num == 3:
            print("Found")
            # break
            continue

        print(num)

    for num in nums:
        for char in "ABC":
            print(num, char)

        print("------")

    for i in range(10):
        print(i)

    for i in range(1, 11):
        print(i)

    x = 0

    while x < 10:
        if num == 3:
            break

        print(x)
        x += 1


if __name__ is "__main__":
    main()
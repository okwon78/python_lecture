def main():

    print("A. Arithmetic Operation")
    # 더하기
    print(3 + 2)
    # 빼기
    print(3 - 2)
    # 곱하기
    print(3 * 2)
    # 나누기
    print(3 / 2)
    # 버림 나누기
    print(3 // 2)
    # 지수
    print(3 ** 2)
    # 나머지
    print(3 % 2)

    print("B. Increment variable")
    num = 1
    # num = num + 1
    num += 1
    # num *= 10
    print(num)

    print("C. Comparison")
    first = 3
    second = 2
    # Equal
    print(first == second)
    # Not Equal
    print(first != second)
    # Greater Than
    print(first > second)
    # Less Than
    print(first < second)
    # Greater or Equal
    print(first >= second)
    # Less or Equal
    print(first >= second)

    print("D. Basic Method")
    print(abs(-3))
    print(round(3.141592))
    print(round(3.141592, 2))

    print("E. Casting to number")
    first = "1"
    second = "2"

    first = int(first)
    second = int(second)

    print(first + second)


if __name__ is "__main__":
    main()

def main() -> None:
    print("INPUT:")
    sum: int = 0
    count: int = 0
    number: int = int(input("Input number: "))
    while number != -1:
        if not number % 2:
            sum += number
            count += 1
        number = int(input("Input number: "))

    print("\nOUTPUT:")
    print(sum / count if count else 0)


if __name__ == '__main__':
    main()
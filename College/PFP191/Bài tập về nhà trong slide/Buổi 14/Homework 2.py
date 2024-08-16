def second_largest(array: list[int]) -> int | str:
    for number in array:
        if number < max(array):
            return number
    return "Not found."


def main() -> None:
    print("INPUT:")
    array: list[int] = sorted(map(int, input().split()), reverse=True)

    print("\nOUTPUT:")
    print(second_largest(array))


if __name__ == '__main__':
    main()
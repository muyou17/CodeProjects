def is_balanced(array: list[int]) -> bool:
    for index in range(len(array)):
        if abs(sum(array[:index]) - sum(array[index:])) <= 5:
            return True
    return False


def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input("Array: ").split()))

    print("\nOUTPUT:")
    print(is_balanced(array))


if __name__ == '__main__':
    main()
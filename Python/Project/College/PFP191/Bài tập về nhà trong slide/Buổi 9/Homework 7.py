def is_splitable(array: list[int]) -> bool:
    for index in range(len(array)):
        if sum(array[:index]) == sum(array[index:]):
            return True
    return False


def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input("Array: ").split()))

    print("\nOUTPUT:")
    print(is_splitable(array))


if __name__ == '__main__':
    main()
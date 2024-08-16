def replace_largest_to_smallest(array: list[int]) -> list[int]:
    highest: int = max(array)
    for index, number in enumerate(array):
        if number == highest:
            array[index] = min(array)
    return array


def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input().split()))

    print("\nOUTPUT:")
    print(replace_largest_to_smallest(array))


if __name__ == '__main__':
    main()
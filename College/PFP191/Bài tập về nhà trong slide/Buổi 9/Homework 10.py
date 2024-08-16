def replace_odd_pairs(array: list[int]) -> list[int]:
    index: int = 0
    while index < len(array):
        if array[index] % 2 and array[index + 1] % 2:
            array[index] = array[index] + array[index + 1]
            del array[index + 1]
        else:
            index += 1
    return array


def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input("Array: ").split()))

    print("\nOUTPUT:")
    print('array = %s' % replace_odd_pairs(array))


if __name__ == '__main__':
    main()
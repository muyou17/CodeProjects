from collections import Counter


def find_dominant_indices(array: list[int]) -> dict[int, tuple] | int:
    return {number: tuple(index for index, integer in enumerate(array) if integer == number)
            for number, count in Counter(array).items() if count >= len(array) / 2} or -1


def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input("Array: ").split()))

    print("\nOUTPUT:")
    print(find_dominant_indices(array))


if __name__ == '__main__':
    main()
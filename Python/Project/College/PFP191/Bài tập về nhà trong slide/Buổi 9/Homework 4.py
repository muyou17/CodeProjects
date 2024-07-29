def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input("Array: ").split()))

    print("\nOUTPUT:")
    print(sum(int(f'{array[index]}{array[index + 1]}') for index in range(0, len(array), 2)))


if __name__ == '__main__':
    main()